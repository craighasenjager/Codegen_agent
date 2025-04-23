
import random

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_empty_positions(board):
    """Returns a list of empty positions on the board."""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def player_move(board):
    """Handles the player's move."""
    while True:
        try:
            move = input("Enter your move (row and column): ").split()
            if len(move) != 2:
                raise ValueError("Please enter two numbers.")
            row, col = map(int, move)
            if row not in range(3) or col not in range(3):
                raise ValueError("Row and column must be between 0 and 2.")
            if board[row][col] != ' ':
                raise ValueError("Cell is already occupied.")
            return row, col
        except ValueError as e:
            print(e)

def computer_move(board):
    """Determines the computer's move using a simple AI."""
    # Check if computer can win in the next move
    for row, col in get_empty_positions(board):
        board[row][col] = 'O'
        if check_winner(board, 'O'):
            return row, col
        board[row][col] = ' '

    # Block player's winning move
    for row, col in get_empty_positions(board):
        board[row][col] = 'X'
        if check_winner(board, 'X'):
            board[row][col] = 'O'
            return row, col
        board[row][col] = ' '

    # Choose a random empty position
    return random.choice(get_empty_positions(board))

def main():
    """Main function to run the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's turn
        row, col = player_move(board)
        board[row][col] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # Computer's turn
        print("Computer's turn:")
        row, col = computer_move(board)
        board[row][col] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
