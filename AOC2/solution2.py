inputFile = open("input.txt", 'r')
listofBoxIDs = []

boxID = inputFile.readline()

lengthOfBoxID = len(boxID)-1

while boxID:
    listofBoxIDs.append(boxID)
    boxID = inputFile.readline()

numOfBoxIDs = len(listofBoxIDs)
indexFirst = 0
indexSecond = 0

for x in range(numOfBoxIDs):
    for y in range(numOfBoxIDs):
        numDiff = lengthOfBoxID
        if (x != y):
            for c in range(lengthOfBoxID):
                if (listofBoxIDs[x][c] == listofBoxIDs[y][c]):
                    numDiff = numDiff - 1

        if (numDiff == 1):
            indexFirst = x
            indexSecond = y
            print("matched strings" + listofBoxIDs[indexFirst] + " " + listofBoxIDs[indexSecond])
            break

for x in range(lengthOfBoxID):
    if(listofBoxIDs[indexFirst][x] == listofBoxIDs[indexSecond][x]):
        print(listofBoxIDs[indexFirst][x], end = '')
