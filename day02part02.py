"""Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

- down X increases your aim by X units.
- up X decreases your aim by X units.
- forward X does two things:
    - It increases your horizontal position by X units.
    - It increases your depth by your aim multiplied by X.
Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""

with open('inputday02.txt') as f:
    contents = f.read()

contents = contents.split('\n')[:-1]

horizontal = 0
depth = 0
aim = 0

for i in range(len(contents)):
    move = contents[i]
    move = move.split()
    direction = move[0]
    if direction == 'forward':
        horizontal += int(move[1])
        depth += (aim * int(move[1]))
    elif direction == 'down':
        aim += int(move[1])
    elif direction == 'up':
        aim -= int(move[1])

print('Horizontal: '+ str(horizontal))
print('depth: '+ str(depth))
print(horizontal*abs(depth))
