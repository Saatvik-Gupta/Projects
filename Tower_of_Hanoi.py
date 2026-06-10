'''
Tower Of Hanoi Game.

*requirements---
3 towers known as pegs(start,auxillary,end)
lets label them them as:-
A->Start Tower
B->Auxillary Tower
c->End Tower
N be the number of discs

Aim--->To transfer all discs from A to C

*Condition---
One disc at a time
no larger discs above smaller ones

complexity---> (2^N-1)
'''

counter=1
#Function Defination...
def Tower(N,start,aux,end): # start=A,aux=B,end=C
    global counter
    if(N==1):
        print(f"Move the disc {counter} from {start}->{end}...")
        counter=counter+1
        return
    Tower(N-1,start,end,aux)
    print(f"Move the disc {counter} from {start}->{end}...")
    counter=counter+1
    Tower(N-1,aux,start,end)
    return

n=int(input("Enter the Number of discs:"))
Tower(n,'A','B','C')   #Function Calling...
    