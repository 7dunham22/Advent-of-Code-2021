"""On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste
time counting its arms, the safe thing to do is to figure out which board will win last and
choose that one. That way, no matter which boards it picks, it will win for sure.

Figure out which board will win last. Once it wins, what would its final score be?"""

with open('inputday04.txt') as f:
    data = f.read()

data = data.split('\n')
calls = data[0].split(',')
calls = [int(x) for x in calls]
data = data[2:]

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

#The only change from part 1 is to this function. Instead of returning the winner, the code appends each winner to an array along with its winning call. Then, grab the last element.
def playGame():
    winners = []
    for call in calls:
        if len(boards) == 0:
            return winners
        boardIndex = 0
        while boardIndex < len(boards):    #Note: I looped through the boards with a while statement, so I could more easily remove the winning boards from the main set of boards.
            board = boards[boardIndex]
            for rowIndex in range(len(board)):
                row = board[rowIndex]
                if call in row:
                    callIndex = row.index(call)
                    boards[boardIndex][rowIndex][callIndex] = 100
            if wins(board):                                         # <= See changes here.
                board.append(call)
                winners.append(board)
                boards.pop(boardIndex)
            else:
                boardIndex += 1
    return "An error occurred"

winners = playGame()
lastWinner = winners[-1]
finalCall = lastWinner.pop()

def scoreWinner(board, call):
    total = 0
    for row in board:
        for num in row:
            if num != 100:
                total += num
    return total * call

print(scoreWinner(lastWinner,finalCall))
