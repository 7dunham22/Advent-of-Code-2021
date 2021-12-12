"""You enter a large cavern full of rare bioluminescent dumbo octopuses! They seem to not like the Christmas lights
on your submarine, so you turn them off for now.

There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and flashes
brightly for a moment when its energy is full. Although your lights are off, maybe you could navigate through the
cave without disturbing the octopuses if you could predict when the flashes of light will happen.

Each octopus has an energy level - your submarine can remotely measure the energy level of each octopus (your puzzle
input). For example:

5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526

The energy level of each octopus is a value between 0 and 9. Here, the top-left octopus has an energy level of 5, the
bottom-right one has an energy level of 6, and so on.

You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses
by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9,
it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An
octopus can only flash at most once per step.)

Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy.

Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are
there after 100 steps?"""


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

step = 0
totalFlashes = 0
while step < 193:
    totalFlashes += incrementGrid(grid)
    step += 1
for row in grid:
    print(row)
print(totalFlashes)
