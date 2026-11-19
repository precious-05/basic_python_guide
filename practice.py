"""A simple two-player tic-tac-toe game."""


def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")


def has_winner(board, player):
    winning_lines = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    return any(all(board[index] == player for index in line) for line in winning_lines)


def play_game():
    board = [str(number) for number in range(1, 10)]
    player = "X"

    for turn in range(9):
        print_board(board)

        while True:
            choice = input(f"Player {player}, choose a position (1-9): ")
            if choice.isdigit() and 1 <= int(choice) <= 9:
                position = int(choice) - 1
                if board[position] not in ("X", "O"):
                    break
            print("Invalid choice. Select an empty position from 1 to 9.")

        board[position] = player
        if has_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    play_game()
