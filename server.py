import socket
import pickle
from _thread import *

board = [[0 for _ in range(9)] for _ in range(9)]
selected_block = None
current_player = 'x'

def threaded_client(conn, player_id):
    global board, selected_block, current_player

    conn.send(pickle.dumps({
        "player_id": player_id,
        "board": board,
        "selected_block": selected_block,
        "current_player": current_player
    }))

    while True:
        try:
            data = pickle.loads(conn.recv(4096))

            board = data["board"]
            selected_block = data["selected_block"]
            current_player = data["current_player"]

            conn.sendall(pickle.dumps({
                "board": board,
                "selected_block": selected_block,
                "current_player": current_player
            }))
        except:
            break

    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.1.6", 5051))  # Use your public IP or 0.0.0.0
server.listen(2)

print("Server started. Waiting for connections...")

current_player_id = 0
while current_player_id < 2:
    conn, addr = server.accept()
    print(f"Player {current_player_id+1} connected:", addr)
    start_new_thread(threaded_client, (conn, current_player_id))
    current_player_id += 1
