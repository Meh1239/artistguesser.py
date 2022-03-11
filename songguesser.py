import simple_chalk
import random

usernames = ["test", "test1"]
passwords = ["test", "test1"]
guesses = 0

with open('songs.txt') as songs:
    x = len(songs.readlines())
    linenum = random.randint(0, x)
    songs.seek(0)
    song = songs.readline(linenum)
with open('artists.txt') as artists:
    artists.seek(0)
    artist = artists.readline(linenum)

print(song)

songprint = song.split()
for x in range(0, len(songprint)):
    printsong = songprint[x]

username = input("Enter your username: ")
password = input("Enter your password: ")
if username in usernames and password in passwords and passwords.index(password) == usernames.index(username):
    print("test")
    while guesses <= 0 and guesses >= 1:
        print(artist)
        print()
        guess = input("Guess song name: ")
else:
    exit()
