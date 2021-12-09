"""Next, you need to find the largest basins so you know what
areas are most important to avoid.

A basin is all locations that eventually flow downward to a single
low point. Therefore, every low point has a basin, although some basins
are very small. Locations of height 9 do not count as being in any basin,
and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including
the low point. The example above has four basins.

Find the three largest basins and multiply their sizes together. In
the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest
basins?"""

with open('inputday09.txt') as f:
    data = f.read()
data = data[:-1]
# data = '''2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678'''

def fillBasin(rowIndex, colIndex):
    target = heatMap[rowIndex][colIndex]
    if target == 9:
        return
    heatMap[rowIndex][colIndex] = 9
    basin.append(target)
    if rowIndex > 0:
        fillBasin(rowIndex-1, colIndex)
    if rowIndex < len(heatMap) - 1:
        fillBasin(rowIndex+1, colIndex)
    if colIndex > 0:
        fillBasin(rowIndex, colIndex-1)
    if colIndex < len(heatMap[rowIndex]) - 1:
        fillBasin(rowIndex, colIndex+1)
    return

data = data.split('\n')
heatMap = [[int(char) for char in row] for row in data]
basins = []
basin = []
for rowIndex in range(len(heatMap)):
    for colIndex in range(len(heatMap[rowIndex])):
        fillBasin(rowIndex,colIndex)
        if basin:
            basins.append(basin)
            basin = []
print(basins)
basinSizes = [len(basin) for basin in basins]
basinSizes.sort()
largestBasins = basinSizes[-3:]
finalProduct = 1
for basin in largestBasins:
    finalProduct *= basin
print(finalProduct)
