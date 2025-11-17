# Q--> Create a random number guessing game with paython

import random

num = random.randint(1,10)
tries =0

while True:
    guess=int(input("Please guess your number between 1 and 10:-"))
    if num == guess:
        tries +=1
        print("you are right you guessad number is {tries} tries")
        break
    elif num <guess:
        tries+=1
        print("go a littel lower")
    elif num >guess:
        print("go a littel higher ")
        tries+=1
    else:
        print("Sorry You are Wrong")
    
