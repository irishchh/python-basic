import random

def game(comp,you):
    #if two values are equal declear a tie!
    if comp == you:
        return None
    #cheack for all posibilities for game
    # r = rock
    # s = sicssor
    # p = papper
     
    elif comp ==  "r":
        if you == "s":
            return False
        elif you == "p":
            return True
    elif comp == "p":
        if you == "r,":
            return False
        elif you == "s":
            return True
    elif comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True



print("computer's turn: rock(r) papper(p) or scissor(s)?")
#Here rando|m moduel can choose between rock papper and sissor its like a computer vs player
randno = random.randint(1, 3)
if randno == 1:
    comp = "r"
elif randno == 2:
    comp = "p"
elif randno == 3:
    comp = "s"

# here players choose betweeen rock papper scissor 

you = input("player's turn: rock(r) papper(p) or scissor(s)?")


a = game(comp,you)
# here a is a variable who store data for comp and palyer

print(f"Computer chose {comp}")
print(f"You chose {you}")
# this prints who wins the game

# this function looks who wins lose or tie
if a == None:
    print("The game is tie")
elif a:
    print("You win")
else:
    print("You Lose!")