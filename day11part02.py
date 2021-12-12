"""It seems like the individual flashes aren't bright enough to navigate. However, you might have a better
option: the flashes seem to be synchronizing!

If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able
to navigate through the cavern. What is the first step during which all octopuses flash?"""

grid = '''4112256372
3143253712
4516848631
3783477137
3746723582
5861358884
4843351774
2316447621
6643817745
6366815868'''
grid = grid.split('\n')
grid = [[int(char) for char in row] for row in grid]

def incrementCell(rowIndex, colIndex):
    if grid[rowIndex][colIndex] != 0:
        grid[rowIndex][colIndex] += 1

def flash(rowIndex, colIndex):
    grid[rowIndex][colIndex] = 0
    if rowIndex > 0:
        incrementCell(rowIndex-1, colIndex)
        if colIndex > 0:
            incrementCell(rowIndex-1, colIndex-1)
        if colIndex < len(grid[rowIndex]) - 1:
            incrementCell(rowIndex-1, colIndex+1)
    if rowIndex < len(grid) - 1:
        incrementCell(rowIndex+1, colIndex)
        if colIndex > 0:
            incrementCell(rowIndex+1, colIndex-1)
        if colIndex < len(grid[rowIndex]) - 1:
            incrementCell(rowIndex+1, colIndex+1)
    if colIndex > 0:
        incrementCell(rowIndex, colIndex-1)
    if colIndex < len(grid[rowIndex]) - 1:
        incrementCell(rowIndex, colIndex+1)
    return 1

def incrementGrid(grid):
    stepFlashes = 0
    for rowIndex in range(len(grid)):
        for colIndex in range(len(grid[rowIndex])):
            grid[rowIndex][colIndex] += 1
            targetElement = grid[rowIndex][colIndex]
    stepFlashes += reviewGrid(grid)
    return stepFlashes

def reviewGrid(grid):
    triggeredFlashes = 0
    for rowIndex in range(len(grid)):
        for colIndex in range(len(grid[rowIndex])):
            if grid[rowIndex][colIndex] > 9:
                triggeredFlashes += flash(rowIndex, colIndex)
    if triggeredFlashes > 0:
        triggeredFlashes += reviewGrid(grid)
    return triggeredFlashes

def test(steps):
    step = 0
    totalFlashes = 0
    while step < steps:
        stepFlashes = incrementGrid(grid)
        step += 1
        if stepFlashes == len(grid)*len(grid[0]):
            return step
        else:
            totalFlashes += stepFlashes
    return step

print(test(1000))
