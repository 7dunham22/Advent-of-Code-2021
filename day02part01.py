# Now, you need to figure out how to pilot this thing.

# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

# - forward X increases the horizontal position by X units.
# - down X increases the depth by X units.
# - up X decreases the depth by X units.

# Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.
# After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)
# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?


with open('inputday02.txt') as f:
    contents = f.read()

contents = contents.split('\n')[:-1]

horizontal = 0
depth = 0

for i in range(len(contents)):
    move = contents[i]
    move = move.split()
    direction = move[0]
    if direction == 'forward':
        horizontal += int(move[1])
    elif direction == 'down':
        depth += int(move[1])
    elif direction == 'up':
        depth -= int(move[1])
print('Horizontal: '+ str(horizontal))
print('depth: '+ str(depth))
print(horizontal*abs(depth))
