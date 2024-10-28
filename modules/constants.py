import chess
NO_ROWS = 8
NO_COLUMNS = NO_ROWS
PIECES_SIZE = 80
SQUARE_SIZE = 100
MENU_HEIGHT = 150
FONT_SIZE = 20
FPS = 60
SELECTED_SQUARE_FRAME_SIZE = 2

WIDTH = NO_COLUMNS * SQUARE_SIZE
HEIGHT = NO_ROWS * SQUARE_SIZE + MENU_HEIGHT
PIECES_OFFSET = (SQUARE_SIZE - PIECES_SIZE) / 2

LIGHT_SQUARES_RGB = "#a5befa"
DARK_SQUARES_RGB = "#67779c"
MENU_RGB = "#327ba8"
FONT_RGB = "#f5fffd"
FRAME_RGB = "#e32222"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FEN_DEFAULT = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
FEN_RANDOM_1 = "8/P1K2p2/b3p2k/8/1p1r1N2/B1pPp3/8/q4R1r w - - 0 1"
FEN_RANDOM_2 = "rnb1kb1r/p1p1pppp/5n2/3p1P1q/8/BPN2Q2/PP1PP1PP/R3KBNR w KQkq - 0 1"

SQUARES_COORDS = []

CHESS_ENGINE_PORT = 12345

# Letters for the file (a-h) and numbers for the rank (8-1)
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ranks = ['8', '7', '6', '5', '4', '3', '2', '1']

for rank in ranks:
    row = []
    for file in files:
        row.append(file + rank)
    SQUARES_COORDS.append(row)

SQUARE_TO_COORDS = {}
for square in chess.SQUARES:
        # Get the square name (e.g., 'a1', 'b2')
        square_name = chess.square_name(square)
        
        # Convert the square number to (x, y) coordinates
        x = chess.square_file(square)  # File (column), e.g., 'a' -> 0, 'b' -> 1
        y = 7 - chess.square_rank(square)  # Rank (row), '1' -> 7, '2' -> 6
        
        # Store in the dictionary
        SQUARE_TO_COORDS[square_name] = (x, y)
