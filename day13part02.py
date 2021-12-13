"""https://adventofcode.com/2021/day/13"""

import numpy as np

# EXTRACT DATA
with open('inputday13.txt') as f:
    data = f.read()
data = data.strip().split('\n')
div = data.index('')
dots = data[:div]
instructions = data[div+1:]
dots = [x.split(',') for x in dots]
dots = [[int(x), int(y)] for [x, y] in dots]

#CREATE PAGE AND FILL WITH DOTS
xMax = max([dot[0] for dot in dots])
yMax = max([dot[1] for dot in dots])
page = np.full(shape=[yMax+1, xMax+1], fill_value='.')
for dot in dots:
    page[dot[1]][dot[0]] = '#'

#FOLD FUNCTION DEFINITION
def fold(axis, degree, page):
    if axis == 'y':
        for y in range(len(page)):
            yDistance = degree-y
            mirror = degree + yDistance
            if mirror >= 0 and mirror <= len(page)-1:
                for x in range(len(page[y])):
                    if page[mirror][x] == '#':
                        page[y][x] = '#'
                        #page[mirror][x] = '#' (Implicit. This step skipped because the latter half is always deleted.)
        page = np.delete(page, slice(degree, len(page)), 0)
    else:
        for y in range(len(page)):
            for x in range(len(page[y])):
                xDistance = degree-x
                mirror = degree + xDistance
                if mirror >= 0 and mirror <= len(page[y])-1:
                    if page[y][mirror] == '#':
                        page[y][x] = '#'
                        #page[y][mirror] = '#'
        page = np.delete(page, slice(degree, len(page[0])), 1)
    return page

#COMMIT FOLDS FOR EACH INSTRUCTION
for instruction in instructions:
    axis = instruction[instruction.index('g')+2]
    degree = int(instruction[instruction.index(axis)+2:])
    page = fold(axis, degree, page)

for line in page:
    line = "".join(line)
    print(line)
