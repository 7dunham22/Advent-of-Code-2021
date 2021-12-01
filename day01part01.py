with open('input.txt') as f:
    contents = f.read()

contents = contents.split()
contents = map(int,contents)

increases = 0
decreases = 0
for i in range(1,len(contents)):
    if contents[i] > contents[i-1]:
        increases += 1
    elif contents[i] <= contents[i-1]:
        decreases += 1
print(increases)
print(decreases)
print(len(contents))
