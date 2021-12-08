"""The crabs don't seem interested in your proposed solution.
Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a
constant rate. Instead, each change of 1 step in horizontal
position costs 1 more unit of fuel than the last: the first
step costs 1, the second step costs 2, the third step costs
3, and so on.

Determine the horizontal position that the crabs can align
to using the least fuel possible so they can make you an
escape route! How much fuel must they spend to align to
that position?"""

with open('inputday07.txt') as f:
    data = f.read()

positions = data.split(',')
positions = [int(x) for x in positions]
positions.sort()

# Test
# positions = [16,1,2,0,4,2,7,1,2,14]
# positions.sort()

maxPosition = max(positions)
minPosition = min(positions)

fuel = []

for pos in range(minPosition, maxPosition + 1):
    fuel.append(0)
    for crab in positions:
        fuel[-1] += sum(range(abs(crab - pos) + 1))

print(min(fuel))
