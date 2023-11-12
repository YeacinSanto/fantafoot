def getData(file):
    try:
        with open(file,"r") as infile:
            line = infile.readline().strip()
            player = []
            while line != "":
                tmpplayer = line.split(", ")
                player.append(tmpplayer)
                line = infile.readline().strip()
        return player
    except Exception as problem:
        print(problem)
        exit()

def getGoalkeeper():
    player = getData("fantafoot.txt")
    keeper = []
    print(f"Goalkeeper --> ")
    for i in range(len(player)):
        if player[i][2] == "goalkeeper":
            keeper.append(player[i])

    budget = 0
    finalKeeper = []
    for j in range(len(keeper)):
        if budget <= 20:
            finalKeeper.append(keeper[j])
            budget += int(keeper[j][3])
    return finalKeeper[0:3]

def getDefender():
    player = getData("fantafoot.txt")
    defender = []
    print(f"Defender -->")
    for i in range(len(player)):
        if player[i][2] == "defender":
            defender.append(player[i])
    finalDefender = []
    budget = 0
    for j in range(len(defender)):
        if budget <= 40 and int(defender[j][3])<15:
            finalDefender.append(defender[j])
            budget = budget + int(defender[j][3])
    return finalDefender[0:8]
def getMidfilder():
    player = getData("fantafoot.txt")
    midfilder = []
    for i in range(len(player)):
        if player[i][2] == "midfielder":
            midfilder.append(player[i])
    budget = 0
    finalmidfielder = []
    for j in range(len(midfilder)):
        if budget <= 80:
            finalmidfielder.append(midfilder[j])
            budget += int(midfilder[j][3])
    return finalmidfielder[0:8]

print(getDefender())
print(getGoalkeeper())
print(getMidfilder())
