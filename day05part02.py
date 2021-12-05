"""Unfortunately, considering only horizontal and vertical lines doesn't give
you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your
list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

You still need to determine the number of points where at least two lines overlap.
Consider all of the lines. At how many points do at least two lines overlap?"""

with open('inputday05.txt') as f:
    data = f.read()

data = data.split('\n')[:-1]
grid = [[0]*1000 for x in range(1000)]

for i in range(len(data)):
    line = data[i].split(' -> ')
    start = line[0].split(',')
    end = line[1].split(',')
    x0 = int(start[0])
    y0 = int(start[1])
    x1 = int(end[0])
    y1 = int(end[1])

    #Measure from the point with the smaller x value for the solution to work.
    if x1 < x0:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    if x0 == x1:
        x = x0
        for y in range(min(y0,y1),max(y0,y1)+1):
            grid[y][x] += 1
    #PART ONE: Use this for horizontal lines with slope 0.
    # elif y0 == y1:
    #     y = y0
    #     for x in range(min(x0,x1),max(x0,x1)+1):
    #         grid[y][x] += 1

    #PART TWO: Instead of the deleted section above, fill x and y according to the direction of the slope, either 1 or -1.
    if x1 > x0:
        dx = x1 - x0
        dy = y1 - y0
        m = dy // dx
        y = y0
        for x in range(x0,x1+1):
            grid[y][x] += 1
            y = y + m

intersections = 0
for row in grid:
    for num in row:
        if num >= 2:
            intersections += 1
print(intersections)
