displaytwo = []
displaythree = []
displayfour = []
global x
x = 1

def leadsort():
    global x
    leaderboard = open("leaderboard.txt", "r+")
    display = leaderboard.readlines()
    for i in range(1,len(display)):
        displaytwo.append(display[i].strip())
    for i in range(0,len(displaytwo)):
        displaythree.append(displaytwo[i].split(":"))
    winslead = open("winslead.txt", "a+")
    pointslead = open("pointslead", "a+")
    for i in range(0,len(displaythree)):
        print(displaythree)
        while i > 0 and int(displaythree[i][1]) > int(displaythree[i - x][1]):
            x += 1
        if i > 0 and x >= 2:
            displayfour.insert(i - (x - 1), displaythree[i])
        else:
            displayfour.append(displaythree[i])
    """for i in range(0,len(displaythree)):
        if i > 0 and int(displaythree[i][2]) > int(displaythree[i - 1][2]):
            displayfour.insert(i - 1,displaythree[i])
        elif i == 0:
            displayfour.append(displaythree[i])
        else:
            displayfour.append(displaythree[i])"""
    print(displayfour)
    

leadsort()
