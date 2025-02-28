#!/usr/bin/python3
import pygame
import chess
import socket
from modules.chess_pieces import *
from modules.board import *
from modules.constants import *

def communicate_with_engine(s, fen):
    s.sendall(fen.encode('utf-8'))
    response = s.recv(1024).decode('utf-8')
    return response

def get_legal_moves(fen):
    board = chess.Board(fen)
    moves_dict = {}
    possible_moves = list(board.legal_moves)

    for move in possible_moves:
        first_square = chess.square_name(move.from_square)
        second_square = chess.square_name(move.to_square)
        if first_square in moves_dict:
            moves_dict[first_square].append(second_square)
        else:
            moves_dict[first_square] = [second_square]
    return moves_dict

def main():
    pygame.init()
    icon = pygame.image.load('/home/maks/mgr/Masalot/assets/Masalot_logo.jpg')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Play with chess engine")
    font = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
    timer = pygame.time.Clock()

    fen = FEN_DEFAULT
    all_fens = [fen] 
    current_fen_index = 0
    player_is_white = False
    white_turn = True
    player_turn = player_is_white
    selected_square = None
    square_1 = None
    square_2 = None
    selected_promotion = 'q'
    promotion_options = ['Queen', 'Rook', 'Knight', 'Bishop']
    menu_rects = []

    run = True
    last_no_moves = 0
    state = 0
    x_coord = 10
    y_coord = 10
    board = chess.Board(fen)

    screen.fill(DARK_SQUARES_RGB)
    draw_promotion_menu(promotion_options, menu_rects)
    draw_board(screen, font, state)
    draw_pieces_from_fen(screen, white_images_list, black_images_list, fen)
    pygame.display.flip()

    if len(all_fens) > last_no_moves:
        last_no_moves = len(all_fens)
        surface = pygame.display.get_surface()
        pygame.image.save(surface, f"screenshots/{len(all_fens)}.png")
        print(f"Screenshot saved as {len(all_fens)}.png")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', CHESS_ENGINE_PORT))
        while run:
            timer.tick(FPS)
            screen.fill(DARK_SQUARES_RGB)
            pygame.draw.rect(screen, MENU_RGB, [0, HEIGHT - MENU_HEIGHT, WIDTH, MENU_HEIGHT])
            draw_board(screen, font, state)

            for i, rect in enumerate(menu_rects):
                pygame.draw.rect(screen, BLACK, rect)
                option_text = font.render(promotion_options[i], True, WHITE)
                screen.blit(option_text, (rect.x + 5, rect.y + 5))


            if not player_turn and current_fen_index == len(all_fens) - 1:
                resp = communicate_with_engine(s, all_fens[-1])  # Get the engine's move
                print(f"Response from engine: {resp}")
                if len(resp) < 8:
                    print(board.push_uci(resp))
                    fen = board.fen()
                else:
                    fen = resp
                    board = chess.Board(fen)

                all_fens.append(fen)  # Store engine's FEN
                current_fen_index += 1  # Update to the new position
                player_turn = True  # Give control back to the player

            if player_turn and current_fen_index == len(all_fens) - 1:  # Allow move only on latest position
                legal_moves = get_legal_moves(all_fens[current_fen_index])
                pygame.draw.rect(
                    screen,
                    FRAME_RGB,
                    [
                        x_coord * SQUARE_SIZE + 1,
                        y_coord * SQUARE_SIZE + 1,
                        SQUARE_SIZE,
                        SQUARE_SIZE,
                    ],
                    SELECTED_SQUARE_FRAME_SIZE,
                )
                if selected_square in legal_moves:
                    for move in legal_moves[selected_square]:
                        pygame.draw.rect(
                            screen,
                            FRAME_RGB,
                            [
                                SQUARE_TO_COORDS[move][0] * SQUARE_SIZE + 1,
                                SQUARE_TO_COORDS[move][1] * SQUARE_SIZE + 1,
                                SQUARE_SIZE,
                                SQUARE_SIZE,
                            ],
                            SELECTED_SQUARE_FRAME_SIZE,
                        )
                if square_1 in legal_moves and square_2 in legal_moves[square_1]:
                    move = chess.Move.from_uci(square_1 + square_2)
                    move_promotion = chess.Move.from_uci(square_1 + square_2 + selected_promotion)
                    if move in board.legal_moves:
                        board.push(move)
                        fen = board.fen()
                        all_fens.append(fen)  # Store the new FEN in the list
                        current_fen_index += 1  # Move to the new position
                        square_1 = None
                        square_2 = None
                        selected_square = None
                        player_turn = False  # Switch to the engine's turn
                    elif move_promotion in board.legal_moves:
                        board.push(move_promotion)
                        fen = board.fen()
                        all_fens.append(fen)  # Store the new FEN in the list
                        current_fen_index += 1  # Move to the new position
                        square_1 = None
                        square_2 = None
                        selected_square = None
                        player_turn = False  # Switch to the engine's turn
                    else:
                        print("TRIED TO EXECUTE ILLEGAL MOVE")
                        pygame.quit()
                    print(f"Players move: {fen}")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and player_turn:
                    if event.pos[0] <= WIDTH and event.pos[1] <= WIDTH:
                        x_coord = event.pos[0] // SQUARE_SIZE
                        y_coord = event.pos[1] // SQUARE_SIZE
                        selected_square = SQUARES_COORDS[y_coord][x_coord]

                    if selected_square in legal_moves:
                        square_1 = selected_square

                    if square_1 in legal_moves and selected_square in legal_moves[square_1]:
                        square_2 = selected_square
                    else:
                        square_1 = selected_square

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and current_fen_index > 0:  # Navigate to previous position
                        current_fen_index -= 1
                    elif event.key == pygame.K_RIGHT and current_fen_index < len(all_fens) - 1:  # Navigate forward
                        current_fen_index += 1
                    elif event.key == pygame.K_HOME:  # Go to the first position
                        current_fen_index = 0

            if len(all_fens) > last_no_moves:
                draw_pieces_from_fen(screen, white_images_list, black_images_list, all_fens[-1])
                pygame.display.flip()

                last_no_moves = len(all_fens)
                surface = pygame.display.get_surface()
                pygame.image.save(surface, f"screenshots/{len(all_fens)}.png")
                print(f"Screenshot saved as {len(all_fens)}.png")
                
            draw_pieces_from_fen(screen, white_images_list, black_images_list, all_fens[current_fen_index])
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    main()
