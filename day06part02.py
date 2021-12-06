"""Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

How many lanternfish would there be after 256 days?"""

with open('inputday06.txt') as f:
    data = f.read();

fish = data.split(',')
fish[-1] = '1' #Manually corrected this data point.
fish = [int(x) for x in fish]

# population = {8: 0, 7: fish.count(7), 6: fish.count(6), 5: fish.count(5), 4: fish.count(4), 3: fish.count(3), 2: fish.count(2), 1: fish.count(1), 0: fish.count(0)}
population = dict(zip([i for i in range(9)], [fish.count(i) for i in range(9)]))

day = 1
while day < 257: #Insert target date here.
    births = 0
    for i in range(8):
        if i == 0:
            births = population[i]
            resets = population[i]
        population[i] = population[i+1]
    population[8] = births
    population[6] += resets
    day += 1

print(population)
print(sum(population.values()))
