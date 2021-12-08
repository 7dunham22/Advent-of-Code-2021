"""A giant whale has decided your submarine is its next meal, and it's
much faster than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too
deep for them otherwise) zooms in to rescue you! They seem to be preparing
to blast a hole in the ocean floor; sensors indicate a massive underground
cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough
power to blast a large enough hole for your submarine to get through.
However, it doesn't look like they'll be aligned before the whale
catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your
puzzle input). Crab submarines have limited fuel, so you need to find
a way to make all of their horizontal positions match while requiring
them to spend as little fuel as possible.

Determine the horizontal position that the crabs can align to using
the least fuel possible. How much fuel must they spend to align to
that position?"""

with open('inputday07.txt') as f:
    data = f.read()

positions = data.split(',')
positions = [int(x) for x in positions]
positions.sort()


median = positions[len(positions)//2]
fuelCost = 0
for i in range(len(positions)):
    localCost = abs(positions[i] - median)
    fuelCost += localCost

print(fuelCost)
