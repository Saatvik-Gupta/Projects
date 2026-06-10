'''
The Perfect Guess...

Computer randomly chooses a number between 1 to 100 and the player has to guess the number
'''

import random

num=random.randint(1,101)  #1 to 100 

a=-1
guesses=0
while(a!=num):

    a=int(input("Guess a number between 1 to 100:"))
    if(a>num):
        print("Guess Lower Number Please!")
    elif(a<num):
        print("Guess Higher Number Please!")
    guesses+=1        

print(f"Player successfully guessed the number {num} in {guesses} attempts...")
print("End Of Game!")