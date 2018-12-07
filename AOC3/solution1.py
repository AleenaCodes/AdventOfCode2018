rows = 1100
cols = 1100

grid = []

for i in range(rows):
    line = []
    for j in range(cols):
        line.append(0)
    grid.append(line)

inputFile = open("input.txt", 'r')
claim = inputFile.readline()

while claim:
    data = claim.split()

    distances = data[2].split(',')
    distances[1] = distances[1][:-1]
    leftDist = int(distances[0])
    topDist = int(distances[1])

    dimensions = data[3].split('x')
    width = int(dimensions[0])
    height = int(dimensions[1])

    for j in range(height):
        for i in range(width):
            grid[topDist+j][leftDist+i] += 1

    claim = inputFile.readline()

answer = 0

for k in range(rows):
    for l in range(cols):
        if grid[k][l] > 1:
            answer += 1

print(answer)
