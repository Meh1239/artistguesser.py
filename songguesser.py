import random

usernames = ["test", "test1"]
passwords = ["test", "test1"]
guesses = 0
printsong = ""
count = 0
wincount = 0
gamecount = 1
global song
with open('songs.txt') as songs:
    songs.seek(0)
    x = len(songs.readlines()) - 1
    linenum = random.randint(0, x)
    songs.seek(0)
    song = songs.readlines(linenum)[0]
with open('artists.txt') as artists:
    artists.seek(0)
    artist = artists.readlines(linenum)[0]

songsplit = song.split()
while count != len(songsplit):
    holder = songsplit[count]
    if count == 0:
        printsong += holder[0]
        for z in range(0, len(holder) - 1):
            printsong += "-"
        count += 1
    else:
        printsong += " " + holder[0]
        for z in range(0, len(holder) - 1):
            printsong += "-"
        count += 1

username = input("Enter your username: ")
password = input("Enter your password: ")
if username in usernames and password in passwords and passwords.index(password) == usernames.index(username):
    while guesses >= 0 and guesses <= 1:
        print("The artist is", artist)
        print("Song hint", printsong)
        guess = input("Guess song name: ")
        if guess == song:
            guesses = 0
            gamecount += 1
            wincount += 1
            print("You have won", wincount, "game(s)")
            x = len(songs.readlines()) - 1
            linenum = random.randint(0, x)
            songs.seek(0)
            song = songs.readlines(linenum)
            song = song[0] #Casts song from array into a str
            artists.seek(0)
            artist = artists.readlines(linenum)
            artist = artist[0] #Casts song from array into a str
            songsplit = song.split()
            while count != len(songsplit):
                holder = songsplit[count]
                if count == 0:
                    printsong += holder[0]
                    for z in range(0, len(holder) - 1):
                        printsong += "-"
                    count += 1
                else:
                    printsong += " " + holder[0]
                    for z in range(0, len(holder) - 1):
                        printsong += "-"
                    count += 1
        else:
            guesses += 1
    print("You lost after", gamecount, "game(s)")
else:
    exit()
