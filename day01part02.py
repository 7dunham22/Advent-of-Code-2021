with open('input.txt') as f:
    contents = f.read()

contents = contents.split()
contents = map(int,contents)

sliderSums = []
i = 0
while (i+2 < len(contents)):
    slider = sum(contents[i:i+3])
    sliderSums.append(slider)
    i+=1

increases = 0
decreases = 0
for i in range(1,len(sliderSums)):
    if sliderSums[i] > sliderSums[i-1]:
        increases += 1
    elif sliderSums[i] <= sliderSums[i-1]:
        decreases += 1
print(increases)
print(decreases)
print(len(sliderSums))
