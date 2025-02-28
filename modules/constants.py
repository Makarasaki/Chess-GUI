import chess
NO_ROWS = 8
NO_COLUMNS = NO_ROWS
PIECES_SIZE = 80
PAWN_SIZE = 65
SQUARE_SIZE = 100
MENU_HEIGHT = 150
FONT_SIZE = 20
FPS = 60
SELECTED_SQUARE_FRAME_SIZE = 2

WIDTH = NO_COLUMNS * SQUARE_SIZE
HEIGHT = NO_ROWS * SQUARE_SIZE + MENU_HEIGHT
PIECES_OFFSET = (SQUARE_SIZE - PIECES_SIZE) / 2
PAWN_OFFSET = (SQUARE_SIZE - PAWN_SIZE) / 2

LIGHT_SQUARES_RGB = "#a5befa"
DARK_SQUARES_RGB = "#67779c"
MENU_RGB = "#327ba8"
FONT_RGB = "#f5fffd"
FRAME_RGB = "#e32222"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FEN_DEFAULT = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
FEN_TEST_STALE = "6k1/5p2/6P1/2n1p1P1/p3b1Kp/P7/8/7q b - - 2 49"
FEN_MIDGAME = "r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10"
FEN_ENDGAME = "5nk1/pp3pp1/2p4p/q7/2PPB2P/P5P1/1P5K/3Q4 w - - 1 28"
FEN_RANDOM_2 = "rnb1kb1r/p1p1pppp/5n2/3p1P1q/8/BPN2Q2/PP1PP1PP/R3KBNR w KQkq - 0 1"
FEN_QP_W = "8/8/8/8/K4k2/PP2p3/1P6/QP6 w - - 0 1"
FEN_FAIL = "rnbq1bnr/1pp2kp1/p3p2p/3p4/6Q1/4P3/PPPP1PPP/RNB1KB1R w KQ - 0 6"
FEN_CRASH = "r2qk1nr/pppb1p1p/2n3p1/1B1pp1N1/8/1P2P3/PBPP1PPP/RN2K2R w KQkq - 2 9"

FEN_TEST = "5N1B/4k3/4pbnr/8/5Q1P/8/8/1K6 w - - 0 1"

SQUARES_COORDS = []

CHESS_ENGINE_PORT = 12346

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
