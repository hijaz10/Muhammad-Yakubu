#while loop, variables, conditionals,input function, print statements, 
#time library(sleep(3))
#random library(randint(), choice())

#todays project is to create a game of chance
#algorithm for the game
#1)give the instructons to the players
#2)choose a door from the list of doors
#3)use the input function to get the players choice
#4)The computer pick the random door for the prize
#5)then we check if our pick is the same as that of the computer using conditionals
#6)our point increases everytime we get the door right

from time import *
from random import *

score=0
attempt=0
#the condition for the game to end is that you must get 3 points
print("""
GAMESHOW!
========
THERE IS A PRIZE BEHIND ONE OF THE 3 DOOR!
GUESS THE RIGHT DOOR TO WIN THE PRIZE
 ____   ____   ____    
|    | |    | |    |
| [1]| |[2] | |[3] |
|   o| |   o| |   o|
|____| |____| |____|

CHOOSE A DOOR (1,2 OR 3):
""")
while score <3:
    #this is where we increase the number of attempts
    attempt=attempt+1
    print("\n you are on attempt number",attempt,"choose a door from (1,2,3)")
    #this is where the player picks a door
    player=int(input())
    #this is where the computer picks a random door
    prizedoor=randint(1,3)
    #this is where we see what we picked
    print("you picked door",player)
    sleep(2)
    #this is where we see the prize door
    print("the prize door is door",prizedoor)
    sleep(2)
    #this is where we compare our picks with the computer
    if player == prizedoor:
        score=score+1
        print("you are right")
    else:
        print("try again")
    print("your current score is",score)
print("CONGRATULATIONS! YOU DID IT IN",attempt,"attempts")
sleep(2)
print("GAMEOVER!")


























