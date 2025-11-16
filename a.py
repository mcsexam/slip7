import math

PLAYER = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]

def check_win(board, player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_terminal(board):
    return check_win(board, PLAYER) or check_win(board, AI) or not get_empty_cells(board)

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, AI):
        return 1
    if check_win(board, PLAYER):
        return -1
    if not get_empty_cells(board):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for move in get_empty_cells(board):
            board[move] = AI
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in get_empty_cells(board):
            board[move] = PLAYER
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = -1
    for move in get_empty_cells(board):
        board[move] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = [EMPTY] * 9
    current_player = PLAYER
    while not check_terminal(board):
        print("\nCurrent Board:")
        print_board(board)
        if current_player == PLAYER:
            try:
                move = int(input("Enter your move (0-8): "))
                if move in range(9) and board[move] == EMPTY:
                    board[move] = PLAYER
                    current_player = AI
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
        else:
            print("AI is thinking...")
            ai_move = find_best_move(board)
            if ai_move != -1:
                board[ai_move] = AI
                current_player = PLAYER
    print("\n--- Final Board ---")
    print_board(board)
    if check_win(board, PLAYER):
        print(" YOU WIN!")
    elif check_win(board, AI):
        print("AI WINS!")
    else:
        print(" IT'S A DRAW!")

if __name__ == "__main__":
    play_game()
