import simple_chalk
import random

usernames = ["test", "test1"]
passwords = ["test", "test1"]
guesses = 0
with open('songs.txt', 'r') as songs:
    count = 0
    for line in fp:
        if line != "\n":
            count += 1
    linenum = random.randint(0, count - 1)
    song = songs.readline(linenum)

with open('artists.txt', 'r') as artists:
    artist = artists.readline(linenum)

print(linenum)
print(song)
songprint = song.split()
for y in range(0, len(songprint)):
    printsong = songprint[y]
username = input("Enter your username: ")
password = input("Enter your password: ")

for z in range(0,len(usernames)):
    if username == usernames[z] and password == passwords[z]:
        while guesses <= 0 and guesses >= 1:
            print(artist)
            print()
            guess = input("Guess song name: ")
    else:
        exit()