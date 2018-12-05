inputFile = open("input.txt", 'r')
answer = 0

freqChange = inputFile.readline()

while freqChange:
    answer += int(freqChange)
    freqChange = inputFile.readline()

inputFile.close()

print(answer)
