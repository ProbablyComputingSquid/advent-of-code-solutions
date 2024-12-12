f = open("day-6/testcase.txt", "r")
f = f.read().split("\n")

global guardXPos
global guardYPos
direction = "up"
# find guard pos
for i in range(len(f)):
    f[i] = list(f[i])
    for j in range(len(f[i])):
        if f[i][j] == "^":
            guardXPos = j
            guardYPos = i
           
        f[i][j] = {
            "block": f[i][j],
            "visited": False,
            "directionsVisited": [],
        }


print("guard at x: ", guardXPos, "y: ", guardYPos)   

log_template = f.copy()


# returns true if guard exits map, false if infinite loop
def runGuard(guardYPos, guardXPos, log):
    direction = "up"
    #print("guard at x: ", guardXPos, "y: ", guardYPos, "direction: ", direction)
    while True:
        log[guardYPos][guardXPos]["visited"] = True
        if direction == "up":
            if guardYPos == 0:
                return True
            if direction in log[guardYPos-1][guardXPos]["directionsVisited"]:
                return False
            else:
                log[guardYPos][guardXPos]["directionsVisited"].append(direction)
            if log[guardYPos-1][guardXPos]["block"] == "#":
                direction = "right"
            else:
                guardYPos -= 1
        elif direction == "right":
            if guardXPos == len(log[0])-1:
                return True
            if direction in log[guardYPos][guardXPos+1]["directionsVisited"]:
                return False
            else:
                log[guardYPos][guardXPos]["directionsVisited"].append(direction)
            if log[guardYPos][guardXPos+1]["block"] == "#":
                direction = "down"
            else:
                guardXPos += 1
        elif direction == "down":
            if guardYPos == len(log)-1:
                return True
            if direction in log[guardYPos+1][guardXPos]["directionsVisited"]:
                return False
            else:
                log[guardYPos][guardXPos]["directionsVisited"].append(direction)
            if log[guardYPos+1][guardXPos]["block"] == "#":
                direction = "left"
            else:
                guardYPos += 1
        elif direction == "left":
            if guardXPos == 0:
                return True
            if direction in log[guardYPos][guardXPos-1]["directionsVisited"]:
                return False
            else:
                log[guardYPos][guardXPos]["directionsVisited"].append(direction)
            if log[guardYPos][guardXPos-1]["block"] == "#":
                direction = "up"
            else:
                guardXPos -= 1



loops = 0
for i in range(len(log_template)):
    for j in range(len(log_template[i])):
        local_log = log_template.copy()
        local_log[i][j]["block"] = "#"
        if not runGuard(guardYPos, guardXPos, local_log.copy()):
            loops += 1
            
    
print(loops)

