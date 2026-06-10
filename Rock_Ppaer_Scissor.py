'''
Rock-Paper-Scissor Game...
Let assume-
    Rock(r)->1
    Paper(p)->0
    Scissor(s)->-1
'''

import random
'''Computer choose a number randomly from---->1,0,-1:'''
computer=random.choice([-1,0,1])

you=input("Player Enter your choice:")
dictchoice={'r':1,'p':0,'s':-1}
playerchoice=dictchoice[you]

reversedict={1:'Rock',0:'Paper',-1:'Scissor'}

print(f"Computer choose {reversedict[computer]}\nPlayer choose {reversedict[playerchoice]}")

if(computer==playerchoice):
    print("It's a Draw!")
else:

    if(computer==-1 and playerchoice==0):
        print("Computer Won!")
    elif(computer==-1 and playerchoice==1):
        print("Player Won!")
    elif(computer==0 and playerchoice==1):
        print("Computer Won!")
    elif(computer==0 and playerchoice==-1):
        print("Player Won!")
    elif(computer==1 and playerchoice==0):
        print("Player Won!")
    elif(computer==1 and playerchoice==-1):
        print("Computer Won!") 
    else:
        print("Something went Wrong!")              