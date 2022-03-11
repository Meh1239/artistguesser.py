import random

usernames = ["test", "test1"]
passwords = ["test", "test1"]
guesses = 0
wincount = 0
gamecount = 1   

def gensong():
    linenum = random.randint(0, len(open("songs.txt").readlines()) - 1)
    global song
    global artist
    song = open("songs.txt").readlines()
    song = song[linenum]
    song = song.strip()
    artist = open("artists.txt").readlines()
    artist = artist[linenum]
    artist = artist.strip()

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
    gensong()
    while guesses >= 0 and guesses <= 1:
        print("The artist is", artist)
        print("Song hint", hintify(song))
        guess = input("Guess song name: ")
        if guess.strip() == song:
            guesses = 0
            gamecount += 1
            wincount += 1
            print("You have won", wincount, "game(s)")
            gensong()
            hintify(song)
        else:
            guesses += 1
    print("You lost after", gamecount, "game(s)")
else:
    exit()
