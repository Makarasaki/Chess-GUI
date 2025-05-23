import pygame
from modules.constants import *

def draw_board(screen, font, status):
        status_txt = ["Select piece!", "Select destination!", "Select promotion piece!"]
        for row in range(NO_ROWS):
            for col in range(row % 2, NO_COLUMNS, 2):
                pygame.draw.rect(screen, LIGHT_SQUARES_RGB, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        screen.blit(font.render(status_txt[status], True, FONT_RGB), (20, HEIGHT - MENU_HEIGHT))


def draw_promotion_menu(promotion_options, menu_rects):
    for i, option in enumerate(promotion_options):
        menu_rect = pygame.Rect(WIDTH - SQUARE_SIZE, HEIGHT - MENU_HEIGHT + i * 30, SQUARE_SIZE, 30)
        menu_rects.append(menu_rect)

def draw_pieces_from_fen(screen, white_images_list, black_images_list, fen=FEN_DEFAULT):
    piece_to_image_index = {
        'P': 0, 'N': 3, 'B': 5, 'R': 4, 'Q': 1, 'K': 2,  # White pieces
        'p': 0, 'n': 3, 'b': 5, 'r': 4, 'q': 1, 'k': 2   # Black pieces
    }

    # Split the FEN
    rows = fen.split(' ')[0].split('/')

    for row_index, row in enumerate(rows):
        col_index = 0
        for char in row:
            if char.isdigit():
                col_index += int(char)  # Skip the number of empty squares
            else:
                if char.isupper():  # White piece
                    piece_image = white_images_list[piece_to_image_index[char]]
                else:  # Black piece
                    piece_image = black_images_list[piece_to_image_index[char]]

                if char in ['P', 'p']:
                    x_pos = col_index * SQUARE_SIZE + PAWN_OFFSET
                    y_pos = row_index * SQUARE_SIZE + PAWN_OFFSET + (PIECES_SIZE - PAWN_SIZE)/2
                else:
                    x_pos = col_index * SQUARE_SIZE + PIECES_OFFSET
                    y_pos = row_index * SQUARE_SIZE + PIECES_OFFSET

                # Draw the piece on the screen
                screen.blit(piece_image, (x_pos, y_pos))

                col_index += 1