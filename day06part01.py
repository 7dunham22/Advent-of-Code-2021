"""The sea floor is getting steeper. Maybe the sleigh keys got carried this way?

A massive school of glowing lanternfish swims past. They must spawn quickly to reach
such large numbers - maybe exponentially quickly? You should model their growth rate
to be sure.

Although you know nothing about this specific species of lanternfish, you make some
guesses about their attributes. Surely, each lanternfish creates a new lanternfish
once every 7 days.

However, this process isn't necessarily synchronized between every lanternfish - one
lanternfish might have 2 days left until it creates another lanternfish, while another
might have 4. So, you can model each fish as a single number that represents the number
of days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer before
it's capable of producing more lanternfish: two more days for its first cycle.

A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is
included as a valid timer value). The new lanternfish starts with an internal timer
of 8 and does not start counting down until the next day.

Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?
"""

with open('inputday06.txt') as f:
    data = f.read();

fish = data.split(',')
fish[-1] = '1' #Manually corrected this data point.
fish = [int(x) for x in fish]

day = 1
while day < 81:
    births = []
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            births.append(8)
        else:
            fish[i] -= 1
    fish.extend(births)
    day += 1


print(len(fish))
