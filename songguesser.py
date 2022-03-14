import random
import datetime
import json

points = 0
usernames = ["test", "test1"]
passwords = ["test", "test1"]
guesses = 0
wincount = 0
gamecount = 1   

#Implement JSON file for leaderboard here https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

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
else:
    exit()
