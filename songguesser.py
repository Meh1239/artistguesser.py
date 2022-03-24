import random
import datetime

points = 0
usernames = ["test", "test1"]
passwords = ["test", "test1"]
guesses = 0
wincount = 0
gamecount = 1   

def leadsort():
    holderarray2 = []
    holderarray3 = []
    scorelead = []
    winlead = []
    x = 1
    leaderboard = open("leaderboard.txt", "r")
    holderarray = leaderboard.readlines()
    leaderboard.seek(0)
    for i in range(1,len(holderarray)):
        holderarray2.append(holderarray[i].strip())
    for i in range(0,len(holderarray2)):
        holderarray3.append(holderarray2[i].split(":"))
    winslead = open("winslead.txt", "a+")
    winslead.truncate(0)
    winslead.seek(0)
    winslead.write("Place:Playername:Score:Consecutive Wins\n")
    pointslead = open("pointslead.txt", "a+")
    pointslead.truncate(0)
    pointslead.seek(0)
    pointslead.write("Place:Playername:Score:Consecutive Wins\n")
    for i in range(0,len(holderarray3)):
        while i > 0 and int(holderarray3[i][1]) > int(holderarray3[i - x][1]):
            x += 1
        if i > 0 and x >= 2:
            if holderarray3[i][1] > holderarray3[0][1] and holderarray3[i][1] > holderarray3[i - 1][1]:
                scorelead.insert(0, holderarray3[i])
            else:
                scorelead.insert(i - x, holderarray3[i])
        else:
            scorelead.append(holderarray3[i])
    for i in range(0,len(scorelead)):
        pointslead.write(f"{i + 1}:{scorelead[i][0]}:{scorelead[i][1]}:{scorelead[i][2]}\n")
    for i in range(0,len(holderarray3)):
        while i > 0 and int(holderarray3[i][1]) > int(holderarray3[i - x][1]):
            x += 1
        if i > 0 and x >= 2:
            if holderarray3[i][1] > holderarray3[0][1] and holderarray3[i][1] > holderarray3[i - 1][1]:
                winlead.insert(0, holderarray3[i])
            else:
                winlead.insert(i - x, holderarray3[i])
        else:
            winlead.append(holderarray3[i])
    for i in range(0,len(winlead)):
        winslead.write(f"{i + 1}:{winlead[i][0]}:{winlead[i][1]}:{winlead[i][2]}\n")

def gensong():
    linenum = random.randint(0, len(open("songs.txt").readlines()) - 1)
    global song
    global artist
    song = open("songs.txt").readlines()
    song = song[linenum].strip().lower()
    artist = open("artists.txt").readlines()
    artist = artist[linenum].strip()

def hintify(word):
    songhint = ""
    count = 0
    songsplit = word.split()
    while count != len(songsplit):
        holder = songsplit[count]
        if count == 0:
            songhint += holder[0]
            for i in range(0, len(holder) - 1):
                songhint += "-"
            count += 1
        else:
            songhint += " " + holder[0]
            for i in range(0, len(holder) - 1):
                songhint += "-"
            count += 1
    return songhint

leadsort()
username = input("""Enter your username
>""")
password = input("""Enter your password
>""")
if username in usernames and password in passwords and passwords.index(password) == usernames.index(username):
    seeleaderboard = input("""Do you wish to see the leadboard
a for all leaderboards
s for score leaderboard
w for consecutive wins leaderboard
anything else to skip leaderboard
>""")
    if seeleaderboard.lower() == "a":
        print("Wins leaderboard")
        leaderboard = open("winslead.txt", "r")
        for i in range(0,len(open("winslead.txt").readlines())):
            leaderboard.seek(0)
            print(leaderboard.readlines()[i],end="")
        leaderboard.close()
        print("Points leaderboard")
        leaderboard = open("pointslead.txt", "r")
        for i in range(0,len(open("pointslead.txt").readlines())):
            leaderboard.seek(0)
            print(leaderboard.readlines()[i],end="")
        leaderboard.close()
    elif seeleaderboard == "s":
        print("Points leaderboard")
        leaderboard = open("pointslead.txt", "r")
        for i in range(0,len(open("pointslead.txt").readlines())):
            leaderboard.seek(0)
            print(leaderboard.readlines()[i],end="")
        leaderboard.close()
    elif seeleaderboard == "w": #ends with elif because ending with a empty else is useless
        print("Wins leaderboard")
        leaderboard = open("winslead.txt", "r")
        for i in range(0,len(open("winslead.txt").readlines())):
            leaderboard.seek(0)
            print(leaderboard.readlines()[i],end="")
        leaderboard.close()
    playername = input("""Enter Player name
>""")
    gensong()
    while guesses >= 0 and guesses <= 1:
        print(f"The artist is {artist}")
        print(f"Song hint {hintify(song)}")
        guess = input("""Guess song name
>""").strip().lower()
        if guess == song:
            if guesses == 0:
                points += 3
            else:
                points += 1
            guesses = 0
            gamecount += 1
            wincount += 1
            print(f"You have won {wincount} game(s) your current score is {points}")
            gensong()
            hintify(song)
        else:
            guesses += 1
    print(f"You lost after {gamecount} game(s) with a total score of {points}")
    leaderboard = open("leaderboard.txt", "a")
    leaderboard.write(f"{playername}:{points}:{wincount}\n")
    leaderboard.close()
else:
    exit()
