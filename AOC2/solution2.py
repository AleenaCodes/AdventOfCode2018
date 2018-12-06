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
            # print("x is " + listofBoxIDs[x])
            # print("y is " + listofBoxIDs[y])

            for c in range(lengthOfBoxID):
                # print("listofBoxIDs[x][c] is " + listofBoxIDs[x][c])
                # print("listofBoxIDs[y][c] is " + listofBoxIDs[y][c])
                if (listofBoxIDs[x][c] == listofBoxIDs[y][c]):
                    numDiff = numDiff - 1
                    # print("incrementing numDiff down to" + str(numDiff))
        # print("for x is " + listofBoxIDs[x] + " and y is " + listofBoxIDs[y] + " the numDiff is " + str(numDiff))

        if (numDiff == 1):
            indexFirst = x
            indexSecond = y
            print("matched strings" + listofBoxIDs[indexFirst] + " " + listofBoxIDs[indexSecond])
            break

for x in range(lengthOfBoxID):
    if(listofBoxIDs[indexFirst][x] == listofBoxIDs[indexSecond][x]):
        print(listofBoxIDs[indexFirst][x], end = '')
