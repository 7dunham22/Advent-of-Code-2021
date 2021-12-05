"""You come across a field of hydrothermal vents on the ocean floor! These vents constantly
produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents
(your puzzle input) for you to review.

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the
coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These
line segments include the points at both ends.

To avoid the most dangerous areas, you need to determine the number of points where at least two
lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total
of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?"""

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
    elif y0 == y1:
        y = y0
        for x in range(min(x0,x1),max(x0,x1)+1):
            grid[y][x] += 1

intersections = 0
for row in grid:
    for num in row:
        if num >= 2:
            intersections += 1
print(intersections)
