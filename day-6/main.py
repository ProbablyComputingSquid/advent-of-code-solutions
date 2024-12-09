f = open("day-6/input.txt", "r")
f = f.read().split("\n")
#print(f)
guardXPos = 0
guardYPos = 0
direction = "up"
for i in range(len(f)):
    f[i] = list(f[i])
    for j in range(len(f[i])):
        if f[i][j] == "^":
            guardXPos = j
            guardYPos = i



#print(f)
print("guard at x: ", guardXPos, "y: ", guardYPos)   
log = f

while True:
    log[guardYPos][guardXPos] = "X"
    if direction == "up":
        if guardYPos == 0:
            break
        if log[guardYPos-1][guardXPos] == "#":
            direction = "right"
        else:
            guardYPos -= 1
    elif direction == "right":
        if guardXPos == len(log[0])-1:
            break
        if log[guardYPos][guardXPos+1] == "#":
            direction = "down"
        else:
            guardXPos += 1
    elif direction == "down":
        if guardYPos == len(log)-1:
            break
        if log[guardYPos+1][guardXPos] == "#":
            direction = "left"
        else:
            guardYPos += 1
    elif direction == "left":
        if guardXPos == 0:
            break
        if log[guardYPos][guardXPos-1] == "#":
            direction = "up"
        else:
            guardXPos -= 1

count = sum(x.count("X") for x in log)
print(count)