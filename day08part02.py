"""Through a little deduction, you should now be able to determine
the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf

After some careful analysis, the mapping between signal wires and
segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc

So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1

Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3

Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above,
the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315

Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the
four-digit output values. What do you get if you add up all of the output values?
"""

with open('inputday08.txt') as f:
    data = f.read()

# data = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

data = data.split('\n')[:-1] #Remove [:-1] when dealing with the test case.
finalTotal = 0
for pattern in data:
    pattern = pattern.split('|')
    inputs = pattern[0].split()
    outputs = pattern[1].split()
    translations = {}
    fives = []
    sixes = []
    for input in inputs:
        if len(input) == 2:
            translations[''.join(sorted(input))] = '1'
        elif len(input) == 3:
            translations[''.join(sorted(input))] = '7'
        elif len(input) == 4:
            translations[''.join(sorted(input))] = '4'
        elif len(input) == 7:
            translations[''.join(sorted(input))] = '8'
        elif len(input) == 5:
            thisInput = ''.join(sorted(input))
            if thisInput not in fives:
                fives.append(set([char for char in thisInput]))
        elif len(input) == 6:
            thisInput = ''.join(sorted(input))
            if thisInput not in sixes:
                sixes.append(set([char for char in thisInput]))
    diffs = []
    for six in sixes:
        thisDiff = []
        for five in fives:
            thisDiff.append(len(six.symmetric_difference(five)))
        diffs.append(thisDiff)
    for i in range(len(diffs)):
        input = sorted(sixes[i])
        if sum(diffs[i]) == 5:
            translations[''.join(input)] = '9'
        elif sum(diffs[i]) == 7:
            translations[''.join(input)] = '6'
        else:
            translations[''.join(input)] = '0'
    diffs = []
    for five in fives:
        thisDiff = []
        for six in sixes:
            thisDiff.append(len(five.symmetric_difference(six)))
        diffs.append(thisDiff)
    for i in range(len(diffs)):
        input = sorted(fives[i])
        if sum(diffs[i]) == 9:
            translations[''.join(input)] = '2'
        elif sum(diffs[i]) == 7:
            translations[''.join(input)] = '3'
        else:
            translations[''.join(input)] = '5'
    thisResult = ''
    for i in range(len(outputs)):
        output = ''.join(sorted(outputs[i]))
        outputs[i] = translations[output]
        thisResult += outputs[i]
    print(thisResult)
    finalTotal += int(''.join(thisResult))

print(finalTotal)
