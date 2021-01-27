
import  random

highest= 10
answer=random.randint(1,10)

print("Please guess a number between 1 and {}:".format((highest)))
guess=int(input())

if guess < 5:
    print("guess higher")
elif guess > 5 :
    print("guess lower")
else :
    print("your guess is right")