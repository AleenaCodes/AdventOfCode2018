inputFile = open("input.txt", 'r')
allLines = []
biggestGuard = 0
guardDatapoint = inputFile.readline()
currentGuard = 0
sleepStartTime = 0
sleepEndTime = 0

# Parse in input into allLines array
while guardDatapoint:
    allLines.append(guardDatapoint)

    data = guardDatapoint.split()

    if (data[2] == "Guard"):
        guardNo = int(data[3][1:])
        if guardNo > biggestGuard:
            biggestGuard = guardNo

    guardDatapoint = inputFile.readline()

# Sort into date order
allLines.sort()

# Make empty array for sleep amounts and array of totals
sleepAmounts = []
sleepTotals = []

for i in range(biggestGuard):
    sleepAmountLine = []
    for j in range(59):
        sleepAmountLine.append(0)
    sleepAmounts.append(sleepAmountLine)

for i in range(biggestGuard):
    sleepTotals.append(0)

# Go through allLine and fill in sleepAmounts
for j in range(len(allLines)):
    data = allLines[j].split()

    splitTime = data[1].split(':')
    minute = splitTime[1][:-1]

    status = data[2]
    if status == "Guard":
        currentGuard = int(data[3][1:])
    elif status == "falls":
        sleepStartTime = int(minute)
    elif status == "wakes":
        sleepEndTime = int(minute)
        guardIndex = currentGuard-1
        timeSlept = sleepEndTime-sleepStartTime

        sleepTotals[guardIndex] += timeSlept

        for i in range(timeSlept):
            sleepAmounts[guardIndex][sleepStartTime+i-1] += 1

    else:
        print("no status!!")

# Go through sleepAmounts and find guard with biggest
sleepAmount = 0
sleepiestGuard = 0

for i in range(len(sleepTotals)):
    if sleepTotals[i] > sleepAmount:
        sleepiestGuard = i
        sleepAmount = sleepTotals[i]

sleepiestGuard += 1

sleepAmount = 0
sleepiestMinute = 0

for i in range(59):
    if sleepAmounts[sleepiestGuard-1][i] > sleepAmount:
        sleepiestMinute = i
        sleepAmount = sleepAmounts[sleepiestGuard-1][i]

sleepiestMinute += 1

print("Guard with biggest sleep time is " + str(sleepiestGuard))
print("SleepiestMinute is " + str(sleepiestMinute))
print("Answer is " + str(sleepiestGuard*sleepiestMinute))
