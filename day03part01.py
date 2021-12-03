"""The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful
things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate).
The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon
rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption
of the submarine? (Be sure to represent your answer in decimal, not binary.)"""

with open('inputday03.txt') as f:
    data = f.read();

data = data.split('\n')[:-1]

gamma = ''
epsilon = ''

for i in range(len(data[0])):
    digitCounts = [0,0]
    for j in range(len(data)):
        num = data[j]
        if num[i] == '0':
            digitCounts[0] += 1
        else:
            digitCounts[1] += 1
    if digitCounts[0] > digitCounts[1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma = int(gamma,2)
epsilon = int(epsilon,2)

print(gamma)
print(epsilon)
print(gamma*epsilon)
