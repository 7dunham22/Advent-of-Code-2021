"""https://adventofcode.com/2021/day/14"""

# rules = '''CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C'''
# polymer = 'NNCB'

with open('inputday14.txt') as f:
    data = f.read()


data = data.strip().split('\n')
polymer = data[0]
rules = data[2:]
rules = [rule.split(' -> ') for rule in rules]
rules = dict(zip([rule[0] for rule in rules], [rule[1] for rule in rules]))

results = []
steps = 10
polymer = [char for char in polymer]
for step in range(steps):
    transformed = ''
    for i in range(len(polymer) - 1):
        rule = ''.join(polymer[i:i+2])
        insertion = rules[rule]
        transformed += polymer[i] + insertion
    transformed += polymer[-1]
    results.append(transformed)
    polymer = [char for char in transformed]
final = results[-1]
finalChars = set(final)
counts = {}
for char in finalChars:
    charCount = final.count(char)
    counts[char] = charCount
maxCount = max(counts.values())
minCount = min(counts.values())
print(maxCount-minCount)
