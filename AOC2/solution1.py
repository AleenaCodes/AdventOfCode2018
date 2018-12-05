numwithTwo = 0
numwithThree = 0

hasTwo = False
hasThree = False

inputFile = open("input.txt", 'r')

line = inputFile.readline()

while line:
    letterDict = {}

    for letter in line:
        if letter in letterDict:
            letterDict[letter] = letterDict[letter]+1
        else:
            letterDict[letter] = 1

    for letter in letterDict:
        if letterDict[letter] == 2:
            hasTwo = True
        if letterDict[letter] == 3:
            hasThree = True

    if hasTwo:
        numwithTwo = numwithTwo + 1
    if hasThree:
        numwithThree = numwithThree + 1

    hasTwo = False
    hasThree = False

    line = inputFile.readline()
    # //check through string
    # //change bools accordingly
    #
    # //add to numWith variables depending on bools
    # // set bools back to false
    # // read new line

checksum = int(numwithTwo) * int(numwithThree)

print("checksum is " + str(checksum))
