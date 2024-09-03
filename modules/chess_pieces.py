import pygame
from modules.constants import PIECES_SIZE

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

white_queen = pygame.image.load('chess_pieces_images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (PIECES_SIZE, PIECES_SIZE))

white_king = pygame.image.load('chess_pieces_images/white king.png')
white_king = pygame.transform.scale(white_king, (PIECES_SIZE, PIECES_SIZE))

white_rook = pygame.image.load('chess_pieces_images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (PIECES_SIZE, PIECES_SIZE))

white_bishop = pygame.image.load('chess_pieces_images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (PIECES_SIZE, PIECES_SIZE))

white_knight = pygame.image.load('chess_pieces_images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (PIECES_SIZE, PIECES_SIZE))

white_pawn = pygame.image.load('chess_pieces_images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (PIECES_SIZE, PIECES_SIZE))

black_queen = pygame.image.load('chess_pieces_images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (PIECES_SIZE, PIECES_SIZE))

black_king = pygame.image.load('chess_pieces_images/black king.png')
black_king = pygame.transform.scale(black_king, (PIECES_SIZE, PIECES_SIZE))

black_rook = pygame.image.load('chess_pieces_images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (PIECES_SIZE, PIECES_SIZE))

black_bishop = pygame.image.load('chess_pieces_images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (PIECES_SIZE, PIECES_SIZE))

black_knight = pygame.image.load('chess_pieces_images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (PIECES_SIZE, PIECES_SIZE))

black_pawn = pygame.image.load('chess_pieces_images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (PIECES_SIZE, PIECES_SIZE))

white_images_list = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images_list = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]

pieces_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']