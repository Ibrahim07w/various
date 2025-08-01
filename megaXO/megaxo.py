import pygame
from copy import deepcopy
from constants import *
import socket
import pickle

window = pygame.display.set_mode((W,H))
pygame.display.set_caption('megaXO')

def mini_check_winner(block):
    for i in range(0,9,3):
        if block[i] == block[i+1] == block[i+2] and block[i] != 0:
            return block[i]
    for i in range(0,3):
        if block[i] == block[i+3] == block[i+6] and block[i] != 0:
            return block[i]
    if block[0] == block[4] == block[8] and block[4] != 0:
        return block[4]
    if block[2] == block[4] == block[6] and block[4] != 0:
        return block[4]
    return False

def check_winner(board):
    for i in range(0, 9 ,3):
        if mini_check_winner(board[i]) == mini_check_winner(board[i+1]) == mini_check_winner(board[i+2]) and mini_check_winner(board[i]):
            return mini_check_winner(board[i])
    for i in range(0,3):
        if mini_check_winner(board[i]) == mini_check_winner(board[i+3]) == mini_check_winner(board[i+6]) and mini_check_winner(board[i]):
            return mini_check_winner(board[i])
    if mini_check_winner(board[0]) == mini_check_winner(board[4]) == mini_check_winner(board[8]) and mini_check_winner(board[4]):
        return mini_check_winner(board[4])
    if mini_check_winner(board[2]) == mini_check_winner(board[4]) == mini_check_winner(board[6]) and mini_check_winner(board[4]):
        return mini_check_winner(board[4])
    return False

def mini_check_full(block):
    for i in block:
        if i == 0:
            return False
    return True

def check_full(board):
    for block in board:
        if (not mini_check_full(block)) or (not mini_check_winner(block)):
            return False
    return True

def block_square_from_mouse(position):
    x, y = position[0], position[1]

    if not (OUTER_PADDING <= x <= W - OUTER_PADDING and OUTER_PADDING <= y <= H - OUTER_PADDING):
        return None  
    
    block = (x - OUTER_PADDING) // BIG_SPAN + ((y - OUTER_PADDING) // BIG_SPAN) * 3
    trimmed_x = x - BIG_SPAN * ((x - OUTER_PADDING) // BIG_SPAN)
    trimmed_y = y - BIG_SPAN * ((y - OUTER_PADDING) // BIG_SPAN)

    if not (INNER_PADDING <= trimmed_x <= BIG_SPAN - INNER_PADDING and INNER_PADDING <= trimmed_y <= BIG_SPAN - INNER_PADDING):
        return None 
    
    small_x = (trimmed_x - INNER_PADDING) // SMALL_SPAN
    small_y = (trimmed_y - INNER_PADDING) // SMALL_SPAN
    square = small_x + small_y * 3
    return (block, square)

def center_from_block_square(block, square):
    block_x = block % 3
    block_y = block // 3
    square_x = square % 3
    square_y = square // 3
    return (round(OUTER_PADDING + block_x * BIG_SPAN + INNER_PADDING + (square_x-0.5) * SMALL_SPAN + SMALL_SPAN), round(OUTER_PADDING + block_y * BIG_SPAN + INNER_PADDING + (square_y-0.5) * SMALL_SPAN + SMALL_SPAN))

def draw_x(window, x, y):
    pygame.draw.line(window, RED, (x + SMALL_SPAN // 2 -SYMBOL_PADDING, y - SMALL_SPAN // 2 +SYMBOL_PADDING), (x - SMALL_SPAN // 2 +SYMBOL_PADDING, y + SMALL_SPAN // 2 -SYMBOL_PADDING), 5)
    pygame.draw.line(window, RED, (x - SMALL_SPAN // 2 +SYMBOL_PADDING, y - SMALL_SPAN // 2 +SYMBOL_PADDING), (x + SMALL_SPAN // 2 -SYMBOL_PADDING, y + SMALL_SPAN // 2 -SYMBOL_PADDING), 5)
def draw_o(window, x, y):
    pygame.draw.circle(window, BLUE, (x,y), SMALL_SPAN//2 - SYMBOL_PADDING, 4)

def update_draw(window, position, board, player):
    result = block_square_from_mouse(position)
    if result is None:
        return  
    block, square = result
    update_board(board, block, square, player)

def draw_selected_block(window, block, player):
    if player == 'o':
        color = BLUE
    elif player == 'x':
        color = RED
    if block == 0:
        pygame.draw.rect(window, color, rect1 )
        pygame.draw.rect(window, color, rect2)
    if block == 1:
        pygame.draw.rect(window, color, rect1 )
        pygame.draw.rect(window, color, rect3)
        pygame.draw.rect(window, color, rect4)
    if block == 2:
        pygame.draw.rect(window, color, rect4)
        pygame.draw.rect(window, color, rect5)
    if block == 3:
        pygame.draw.rect(window, color, rect2)
        pygame.draw.rect(window, color, rect6)
        pygame.draw.rect(window, color, rect7)
    if block == 4:
        pygame.draw.rect(window, color, rect3)
        pygame.draw.rect(window, color, rect6)
        pygame.draw.rect(window, color, rect8)
        pygame.draw.rect(window, color, rect9)
    if block == 5:
        pygame.draw.rect(window, color, rect5)
        pygame.draw.rect(window, color, rect9)
        pygame.draw.rect(window, color, rect10)
    if block == 6:
        pygame.draw.rect(window, color, rect7)
        pygame.draw.rect(window, color, rect11)
    if block == 7:
        pygame.draw.rect(window, color, rect8)
        pygame.draw.rect(window, color, rect11)
        pygame.draw.rect(window, color, rect12)
    if block == 8:
        pygame.draw.rect(window, color, rect10)
        pygame.draw.rect(window, color, rect12)

def draw(window, board, text=None):
    window.fill(WHITE)
    for rect in VERTICAL_RECTS:
        pygame.draw.rect(window, BLACK, rect)
    for rect in HORIZONTAL_RECTS:
        pygame.draw.rect(window, BLACK, rect)
    for rect in VRECTS:
        pygame.draw.rect(window, GREY, rect)
    for rect in HRECTS:
        pygame.draw.rect(window, GREY, rect)
    for block in range(9):
        for square in range(9):
            x, y = center_from_block_square(block, square)
            if board[block][square] == 'x':
                draw_x(window, x, y)
            elif board[block][square] == 'o':
                draw_o(window, x, y)
    if text:
        rendered_text = FONT.render(text, 1, BLACK)
        window.blit(rendered_text, (W//2 - rendered_text.get_width()//2, 0))

def create_board():
    board = []
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(0)
    return board

def update_board(board, block, square, player):
    if board[block][square] == 0:
        board[block][square] = player
    else:
        print('choose another location')

def change_player(player):
    if player == 'o':
        return 'x'
    else:
        return 'o'

def ai_move(newboard):
    board = newboard
    change_player('o')

def evaluate(board):
    x_wins = o_wins = 0
    for block in board:
        if mini_check_winner(block) == 'o':
            o_wins += 1
        elif mini_check_winner(block) == 'x':
            x_wins += 1
    return o_wins - x_wins

def get_all_moves(board, selected_block, player):
    moves = []
    if selected_block is not None:
        for square in range(9):
            if board[selected_block][square] == 0:
                temp_board = deepcopy(board)
                temp_board[selected_block][square] = player
                moves.append((temp_board, selected_block,square))
    else:
        for block in range(9):
            if not mini_check_winner(board[block]):
                for square in range(9):
                    if board[block][square] == 0:
                        temp_board = deepcopy(board)
                        temp_board[block][square] = player
                        moves.append((temp_board, block, square))
    return moves

def minimax(board, depth, max_player, selected_block, alpha=float('-inf'), beta=float('inf')):
    winner = check_winner(board)
    if depth == 0 or winner:
        if winner == 'o':
            return 10000, board, None, None 
        elif winner == 'x':
            return -10000, board, None, None  
        else:
            return evaluate(board), board, None, None  
    if max_player:
        maxEval = float('-inf')
        best_move = None
        best_block = None
        best_square = None
        for move, block, square in get_all_moves(board, selected_block, 'o'):
            if mini_check_winner(move[square]) or mini_check_full(move[square]):
                next_selected_block = None
            else:
                next_selected_block = square
            evaluation, _, _, _ = minimax(move, depth-1, False, next_selected_block, alpha, beta)
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
                best_block = block
                best_square = square
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return maxEval, best_move, best_block, best_square

    else:
        minEval = float('inf')
        best_move = None
        best_block = None
        best_square = None
        for move, block, square in get_all_moves(board, selected_block, 'x'):
            if mini_check_winner(move[square]) or mini_check_full(move[square]):
                next_selected_block = None
            else:
                next_selected_block = square
            evaluation, _, _, _ = minimax(move, depth-1, True, next_selected_block, alpha, beta)
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
                best_block = block
                best_square = square
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return minEval, best_move, best_block, best_square
    
def mainf():
    run = True
    clock = pygame.time.Clock()
    board = create_board()
    player = 'x'
    selected_block = None
    text = 0
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                result = block_square_from_mouse(position)
                if result is not None:
                    block, square = result
                    if selected_block is None or block == selected_block:
                        if board[block][square] == 0:
                            update_board(board, block, square, player)
                            if mini_check_winner(board[square]) or mini_check_full(board[square]):
                                selected_block = None  
                            else:
                                selected_block = square
                            player = change_player(player)
                        else:
                            text = 'square is already taken'
                    else:
                        text = f'please play in block {selected_block+1}'
        draw(window, board, text)
        draw_selected_block(window, selected_block, player)
        pygame.display.update()
        if check_winner(board):
            text = f'the winner is player {check_winner(board)}'
            rendered_text = FONT.render(text, 1, BLACK)
            window.blit(rendered_text, (W//2 - rendered_text.get_width()//2, H//2 - rendered_text.get_height()//2))
            print('win')
            pygame.time.delay(3000)
            pygame.quit()
        if check_full(board):
            text = 'tie'
            rendered_text = FONT.render(text, 1, BLACK)
            window.blit(rendered_text, (W//2 - rendered_text.get_width()//2, H//2 - rendered_text.get_height()//2))
            pygame.time.delay(3000)
            pygame.quit()
    pygame.quit()

def mains():
    run = True
    clock = pygame.time.Clock()
    board = create_board()
    player = 'x'
    selected_block = None
    text = ''

    while run:
        clock.tick(60)
        if player == 'o':
            value, new_board, last_block, last_square = minimax(board, 6, True, selected_block)
            board = new_board
            if last_square is None:
                selected_block = None
            elif mini_check_winner(board[last_square]) or mini_check_full(board[last_square]):
                selected_block = None
            else:
                selected_block = last_square
            player = change_player(player)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    result = block_square_from_mouse(position)
                    if result is not None:
                        block, square = result
                        if selected_block is None or block == selected_block:
                            if board[block][square] == 0:
                                update_board(board, block, square, player)
                                if mini_check_winner(board[square]) or mini_check_full(board[square]):
                                    selected_block = None
                                else:
                                    selected_block = square
                                player = change_player(player)
                                text = ''
                            else:
                                text = 'Square is already taken'
                        else:
                            text = f'Please play in block {selected_block + 1}'
        draw(window, board, text)
        draw_selected_block(window, selected_block, player)
        pygame.display.update()
        winner = check_winner(board)
        if winner:
            text = f'The winner is player {winner}'
            rendered_text = FONT.render(text, 1, BLACK)
            window.blit(rendered_text, (W // 2 - rendered_text.get_width() // 2, H // 2 - rendered_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(3000)
            run = False
        if check_full(board):
            text = 'Tie!'
            rendered_text = FONT.render(text, 1, BLACK)
            window.blit(rendered_text, (W // 2 - rendered_text.get_width() // 2, H // 2 - rendered_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(3000)
            run = False
    pygame.quit()

def mainn():
    run = True
    clock = pygame.time.Clock()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.1.6", 5051))  # Replace with your public IP
    data = pickle.loads(client.recv(4096))
    board = data["board"]
    selected_block = data["selected_block"]
    player_id = data["player_id"]
    player = 'x' if player_id == 0 else 'o'
    text = ''
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and player == data["current_player"]:
                position = pygame.mouse.get_pos()
                result = block_square_from_mouse(position)
                if result is not None:
                    block, square = result
                    if selected_block is None or block == selected_block:
                        if board[block][square] == 0:
                            board[block][square] = player
                            if mini_check_winner(board[square]) or mini_check_full(board[square]):
                                selected_block = None
                            else:
                                selected_block = square
                            current_player = 'x' if player == 'o' else 'o'

                            send_data = {
                                "board": board,
                                "selected_block": selected_block,
                                "current_player": current_player
                            }
                            client.send(pickle.dumps(send_data))
                            data = pickle.loads(client.recv(4096))
        
        if player != data["current_player"]:
            try:
                client.send(pickle.dumps({
                    "board": board,
                    "selected_block": selected_block,
                    "current_player": data["current_player"]
                }))
                data = pickle.loads(client.recv(4096))
                board = data["board"]
                selected_block = data["selected_block"]
            except:
                pass

        draw(window, board, text)
        draw_selected_block(window, selected_block, data["current_player"])
        pygame.display.update()
        if check_winner(board):
            text = f'The winner is player {check_winner(board)}'
            pygame.time.delay(3000)
            run = False
        if check_full(board):
            text = 'Tie!'
            pygame.time.delay(3000)
            run = False
    client.close()

def start_screen():
    run = True
    while run:
        window.fill(BLACK)
        single = pygame.Rect(150, 50, 300, 100)
        single_text = FONT.render('single player', 1, RED)
        pygame.draw.rect(window, GREY, single)
        window.blit(single_text, (W//2 - single_text.get_width()//2, 100 - single_text.get_height()//2))

        multiplayer = pygame.Rect(150, 200, 300, 100)
        multiplayer_text = FONT.render('multiplayer', 1, RED)
        pygame.draw.rect(window, GREY, multiplayer)
        window.blit(multiplayer_text, (W//2 - single_text.get_width()//2, 250 - single_text.get_height()//2))

        online = pygame.Rect(150, 350, 300, 100)
        online_text = FONT.render('online', 1, RED)
        pygame.draw.rect(window, GREY, online)
        window.blit(online_text, (W//2 - single_text.get_width()//2, 400 - single_text.get_height()//2))

        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if 150 <= position[0] <= 450 and 50 <= position[1] <= 150:
                        mains()
                        run = False
                    elif 150 <= position[0] <= 450 and 200 <= position[1] <= 3000:
                        mainf()
                        run = False
                    elif 150 <= position[0] <= 450 and 350 <= position[1] <= 450:
                        mainn()
                        run = False

start_screen()
