import simple_chalk
import random

usernames = [test, test1]
passwords = [test, test1]
guesses = 0
x = len(file.readlines() - 1)

with open('song', 'r') as file:
    song = file.readline(random.randint(0, x))
with open('artists', 'r') as file:
    artist = file.readline(random.randint(0, x))

songprint = song.split()
for x in range(0, len(songprint)):
    printsong = songprint[x]
username = input("Enter your username: ")
password = input("Enter your password: ")

for x in range(0,len(usernames)):
    if username == usernames[x] and password == passwords[x]:
        while guesses <= 0 and guesses >= 1:
            print(artist)
            print()
            guess = input("Guess song name: ")
    else:
        exit()