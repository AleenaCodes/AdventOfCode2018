rows = 1100
cols = 1100

grid = []
claimOverlapStatus = {}

for i in range(rows):
    line = []
    for j in range(cols):
        line.append(0)
    grid.append(line)

inputFile = open("input.txt", 'r')
claim = inputFile.readline()

while claim:
    data = claim.split()

    data[0] = data[0][1:]
    claimNo = int(data[0])
    claimOverlapStatus[claimNo] = True

    distances = data[2].split(',')
    distances[1] = distances[1][:-1]
    leftDist = int(distances[0])
    topDist = int(distances[1])

    dimensions = data[3].split('x')
    width = int(dimensions[0])
    height = int(dimensions[1])

    for j in range(height):
        for i in range(width):
            if (grid[topDist+j][leftDist+i] != 0):
                overlappingClaim1 = grid[topDist+j][leftDist+i]
                claimOverlapStatus[overlappingClaim1] = False # prev claim on that square is no invalid
                claimOverlapStatus[claimNo] = False # current claim being processed is also invalid
            else:
                grid[topDist+j][leftDist+i] = claimNo

    claim = inputFile.readline()

for k, v in claimOverlapStatus.items():
    if (v == True):
        print(k)
