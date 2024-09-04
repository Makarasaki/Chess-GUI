import pygame
import chess
import socket
from modules.chess_pieces import *
from modules.board import *
from modules.constants import *
import time




def get_legal_moves(fen):
    board = chess.Board(fen)
    moves_dict = {}

    # Get all possible moves
    possible_moves = list(board.legal_moves)

    # Collect moves from each starting square
    for move in possible_moves:
        first_square = chess.square_name(move.from_square)
        second_square = chess.square_name(move.to_square)

        # Add the move to the dictionary
        if first_square in moves_dict:
            moves_dict[first_square].append(second_square)
        else:
            moves_dict[first_square] = [second_square]
    return moves_dict


def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Play with chess engine")
    font = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
    timer = pygame.time.Clock()

    fen = FEN_RANDOM_2
    player_is_white = True
    white_turn = True
    player_turn = player_is_white
    selected_square = None
    square_1 = None
    square_2 = None
    ready_for_square_2 = False

    run = True
    state = 0
    x_coord = 10
    y_coord = 10
    board = chess.Board(fen)

    while run:
        timer.tick(FPS)
        screen.fill(DARK_SQUARES_RGB)
        pygame.draw.rect(
            screen, MENU_RGB, [0, HEIGHT - MENU_HEIGHT, WIDTH, MENU_HEIGHT]
        )
        draw_board(screen, font, state)
        draw_pieces_from_fen(screen, white_images_list, black_images_list, fen)

        if not player_is_white:
            # chess engine move
            pass

        if player_turn:
            legal_moves = get_legal_moves(fen)
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
                print(legal_moves[selected_square])
                for move in legal_moves[selected_square]:
                    print(move, SQUARE_TO_COORDS[move][0], SQUARE_TO_COORDS[move][1])
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
                print("do move:", square_1, square_2)
                move = chess.Move.from_uci(square_1 + square_2)
                if move in board.legal_moves:
                    board.push(move)
                    fen = board.fen()
                    square_1 = None
                    square_2 = None
                    player_turn = False
                else:
                    print("TRIED TO EXECUTE ILLEGAL MOVE")
                    pygame.quit()
            # player_turn = False
            pass
        else:

            # code here

            # player_turn = True
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and player_turn:
                if event.pos[0] <= WIDTH and  event.pos[1] <= WIDTH:
                    x_coord = event.pos[0] // SQUARE_SIZE
                    y_coord = event.pos[1] // SQUARE_SIZE
                    selected_square = SQUARES_COORDS[y_coord][x_coord]
                else:
                    # menu
                    pass

                
                if selected_square in legal_moves:
                    square_1 = selected_square

                if square_1 in legal_moves and selected_square in legal_moves[square_1]:
                    square_2 = selected_square
                else:
                    square_1 = selected_square


        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
