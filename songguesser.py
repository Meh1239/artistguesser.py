import random
import datetime

displaytwo = []
displaythree = []
displayfour = []
points = 0
usernames = ["test", "test1"]
passwords = ["test", "test1"]
guesses = 0
wincount = 0
gamecount = 1   

def leadsort(): #needs to be sorted
    leaderboard = open("leaderboard.txt", "r+")
    display = leaderboard.readlines()
    for i in range(1,len(display)):
        displaytwo.append(display[i].strip())
    for i in range(0,len(displaytwo)):
        displaythree.append(displaytwo[i].split(":"))
    winslead = open("winslead.txt", "a+")
    pointslead = open("pointslead", "a+")
    for i in range(0,len(displaythree)):
        if i > 0 and int(displaythree[i][1]) > int(displaythree[i - 1][1]):
            displayfour.insert(i - 1,displaythree[i])
        elif i == 0:
            displayfour.append(displaythree[i])
        else:
            displayfour.append(displaythree[i])
    for i in range(0,len(displaythree)):
        if i > 0 and int(displaythree[i][2]) > int(displaythree[i - 1][2]):
            displayfour.insert(i - 1,displaythree[i])
        elif i == 0:
            displayfour.append(displaythree[i])
        else:
            displayfour.append(displaythree[i])

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

username = input("Enter your username: ")
password = input("Enter your password: ")
if username in usernames and password in passwords and passwords.index(password) == usernames.index(username):
    playername = input("Enter Player name:")
    gensong()
    while guesses >= 0 and guesses <= 1:
        print(f"The artist is {artist}")
        print(f"Song hint {hintify(song)}")
        guess = input("Guess song name: ").strip().lower()
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
    leaderboard.write(f"{playername}:{points}:{gamecount}:{wincount}\n")
else:
    exit()
