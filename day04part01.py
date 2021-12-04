"""You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight.
What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number
is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of
a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates
a random order in which to draw numbers and a random set of boards (your puzzle input).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case,
the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?"""

# Open and read file
with open('inputday04.txt') as f:
    data = f.read()

data = data.split('\n')
calls = data[0].split(',')
calls = [int(x) for x in calls]
data = data[2:]

#Process the data
boards = []
board = []
for i in range(len(data)):
    row = data[i]
    if row == '':
        boards.append(board)
        board = []
    else:
        row = row.split()
        row = [int(x) for x in row]
        board.append(row)

#Does this board get bingo?
def wins(board):
    for row in board:
        if sum(row) == 500:
            return True
    for i in range(5):
        col = []
        for row in board:
            col.append(row[i])
        if sum(col) == 500:
            return True
    return False

#Find the board that gets bingo. Return the board with the winning call appended to it.
def playGame():
    for call in calls:
        for boardIndex in range(len(boards)):
            board = boards[boardIndex]
            for rowIndex in range(len(board)):
                row = board[rowIndex]
                if call in row:
                    callIndex = row.index(call)
                    boards[boardIndex][rowIndex][callIndex] = 100
            if wins(board):
                board.append(call)
                return board
    return "An error occurred"

winner = playGame()
call = winner.pop()
print(winner)
print(call)

#What is the winner's final score?
def scoreWinner(board, call):
    total = 0
    for row in board:
        for num in row:
            if num != 100:
                total += num
    return total * call

print(scoreWinner(winner,call))
