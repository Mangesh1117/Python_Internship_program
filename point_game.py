import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]
rows = 6
cols = 7

turns = ["🔴", "🔵"]
turnCounter = 0

def printGameBoard():
    print("\n     A    B    C    D    E    F    G")
    for x in range(rows):
        print("   +----+----+----+----+----+----+----+")
        print(f"{x}  |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
                print(f" {gameBoard[x][y]} ", end="|")
            elif gameBoard[x][y] == "🔴":
                print(f" {gameBoard[x][y]} ", end="|")
            else:
                print("    ", end="|")
        print()  # Move to the next row
    print("   +----+----+----+----+----+----+----+")

def checkWin(player):
    # Check horizontal
    for row in range(rows):
        for col in range(cols-3):
            if all(gameBoard[row][col+i] == player for i in range(4)):
                return True

    for col in range(cols):
        for row in range(rows-3):
            if all(gameBoard[row+i][col] == player for i in range(4)):
                return True

    for row in range(rows-3):
        for col in range(cols-3):
            if all(gameBoard[row+i][col+i] == player for i in range(4)):
                return True

    for row in range(3, rows):
        for col in range(cols-3):
            if all(gameBoard[row-i][col+i] == player for i in range(4)):
                return True

    return False

def isDraw():
    for col in range(cols):
        if gameBoard[0][col] == "":
            return False
    return True

while True:
    currentPlayer = turns[turnCounter % 2]

    printGameBoard()
    print(f"\nPlayer {currentPlayer}'s turn")

    columnInput = input("Pick a column (A-G): ").upper()

    if columnInput not in possibleLetters:
        print("Invalid column! Please choose a letter between A and G.")
        continue

    colIndex = possibleLetters.index(columnInput)

    placed = False
    for row in range(rows-1, -1, -1):
        if gameBoard[row][colIndex] == "":
            gameBoard[row][colIndex] = currentPlayer
            placed = True
            break

    if not placed:
        print("This column is full! Please choose another one.")
        continue

    if checkWin(currentPlayer):
        printGameBoard()
        print(f"\nPlayer {currentPlayer} wins!")
        break

    if isDraw():
        printGameBoard()
        print("\nIt's a draw!")
        break

    turnCounter += 1
