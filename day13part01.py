"""https://adventofcode.com/2021/day/13"""

import numpy as np

# data = '''6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0'''

# dots = data.strip().split('\n')
# dots = [x.split(',') for x in dots]
# dots = [[int(x), int(y)] for [x, y] in dots]
# instructions = ['fold along y=7', 'fold along x=5']

with open('inputday13.txt') as f:
    data = f.read()
data = data.strip().split('\n')
div = data.index('')
dots = data[:div]
instructions = data[div+1:]
dots = [x.split(',') for x in dots]
dots = [[int(x), int(y)] for [x, y] in dots]

xMax = 0
yMax = 0
for dot in dots:
    x = dot[0]
    y = dot[1]
    if x > xMax:
        xMax = x
    if y > yMax:
        yMax = y

page = np.full((yMax+1, xMax+1), '.')
for dot in dots:
    page[dot[1]][dot[0]] = '#'


def fold(axis, degree, page):
    if axis == 'y':
        for y in range(len(page)):
            yDistance = degree-y
            mirror = degree + yDistance
            if mirror >= 0 and mirror <= len(page)-1:
                for x in range(len(page[y])):
                    if page[y][x] == '#' or page[mirror][x] == '#':
                        page[y][x] = '#'
                        page[mirror][x] = '#'
        page = np.delete(page, slice(degree, len(page)), 0)
    else:
        for y in range(len(page)):
            for x in range(len(page[y])):
                xDistance = degree-x
                mirror = degree + xDistance
                if mirror >= 0 and mirror <= len(page[y])-1:
                    if page[y][x] == '#' or page[y][mirror] == '#':
                        page[y][x] = '#'
                        page[y][mirror] = '#'
        page = np.delete(page, slice(degree, len(page[0])), 1)
    return page


print(len(page[0]))
instruction = instructions[0]
axis = instruction[instruction.index('g')+2]
degree = int(instruction[instruction.index(axis)+2:])
print(degree)
page = fold(axis, degree, page)

# for line in page:
#     print(line)
# print(page.flatten())
# print(len(page[0]))
print(list(page.flatten()).count('#'))
