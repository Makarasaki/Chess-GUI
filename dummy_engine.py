import chess
import socket
import random
import time

def get_random_move(fen):
    board = chess.Board(fen)
    legal_moves = list(board.legal_moves)
    
    if legal_moves:
        move = random.choice(legal_moves)
        board.push(move)
    
    return board.fen()

def start_dummy_engine(host='localhost', port=12347):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Dummy chess engine listening on {host}:{port}")
        
        client_socket, addr = server_socket.accept()
        with client_socket:
            while True:
                print(f"Connected by {addr}")
                data = client_socket.recv(1024)
                if not data:
                    break
                
                fen = data.decode('utf-8')
                print(f"Received FEN: {fen}")
                
                new_fen = get_random_move(fen)
                time.sleep(1)
                print(f"Sending new FEN: {new_fen}")
                client_socket.sendall(new_fen.encode('utf-8'))

if __name__ == "__main__":
    start_dummy_engine()
