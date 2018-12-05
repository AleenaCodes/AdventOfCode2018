inputFile = open("input.txt", 'r')
listofFreqChanges = []

freqChange = inputFile.readline()

while freqChange:
    listofFreqChanges.append(int(freqChange))
    freqChange = inputFile.readline()

answer = 0
frequencies = set()
frequencies.add(answer)
foundDuplicate = False
iter = 0

while not foundDuplicate:
    answer += listofFreqChanges[iter]

    if answer in frequencies:
        foundDuplicate = True
        print("repeat is " + str(answer))
        break

    frequencies.add(answer)
    iter = (iter+1) % (len(listofFreqChanges))

inputFile.close()

print(answer)
