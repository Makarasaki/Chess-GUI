import pygame
import chess
from modules.chess_pieces import *
from modules.board import *
from modules.constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('Play with chess engine')
    font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
    timer = pygame.time.Clock()

    run = True
    status = 0

    while run:
        timer.tick(FPS)
        screen.fill(DARK_SQUARES_RGB)
        pygame.draw.rect(screen, MENU_RGB, [0, HEIGHT - MENU_HEIGHT, WIDTH, MENU_HEIGHT])
        draw_board(screen, font, status)
        draw_pieces_from_fen(screen, white_images_list, black_images_list, FEN_RANDOM_1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()