"""Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part.
Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with
the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

- Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
- If you only have one number left, stop; this is the rating value for which you are searching.
- Otherwise, repeat the process, considering the next bit to the right.

The bit criteria depends on which type of rating value you want to find:

- To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 1 in the position being considered.
- To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If
    0 and 1 are equally common, keep values with a 0 in the position being considered.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life
support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""

with open('inputday03.txt') as f:
    data = f.read();

data = data.split('\n')[:-1]

def reduce(data, operator):
    for i in range(len(data[0])):
        ones = []
        zeroes = []
        dataCounts = [0,0]
        for j in range(len(data)):
            num = data[j]
            if num[i] == '0':
                dataCounts[0] += 1
                zeroes.append(num)
            else:
                dataCounts[1] += 1
                ones.append(num)
        if dataCounts[0] > dataCounts[1]:
            majority = zeroes
            minority = ones
        elif dataCounts[0] == dataCounts[1] and operator == '<':
            majority = ones
            minority = zeroes
        else:
            majority = ones
            minority = zeroes
        if operator == '>':
            data = majority
        else:
            data = minority
        if len(data) <= 1:
            return data
    return data

oxygenData = reduce(data,'>')[0]
co2Data = reduce(data,'<')[0]
print(int(oxygenData,2) * int(co2Data,2))
