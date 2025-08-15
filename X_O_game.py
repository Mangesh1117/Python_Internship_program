board = [" " for _ in range(9)]
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def is_draw():
    return " " not in board
def tic_tac_toe():
    current_player = "X"
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 9.")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw():
            print_board()
            print("It's a draw! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"
tic_tac_toe()
