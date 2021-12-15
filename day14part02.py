"""https://adventofcode.com/2021/day/14"""

from collections import Counter

with open('inputday14.txt') as f:
    data = f.read()
data = data.strip().split('\n')
polymer = data[0]
rules = data[2:]
rules = [rule.split(' -> ') for rule in rules]
rules = dict(zip([rule[0] for rule in rules], [rule[1] for rule in rules]))

counts = Counter()
for x in range(len(polymer[:-1])):
    counts[polymer[x:x+2]] += 1

for i in range(40):
    countsCopy = counts
    counts = Counter()
    for key in countsCopy.keys():
        counts[key[0] + rules[key]] += countsCopy[key]
        counts[rules[key] + key[1]] += countsCopy[key]

l = Counter()
l[polymer[0]] = 1
for key, count in counts.items():
    l[key[1]] += count

print(l.most_common()[0][1] - l.most_common()[-1][1])
