import random

def Game(comp,player):
    print("Computer chooses: "+comp)
    if(comp=="s" and player=="w"):
        return False
    elif(comp=="s" and player=="g"):
        return True
    elif(comp=="w" and player=="g"):
        return False
    elif(comp=="w" and player=="s"):
        return True
    elif(comp=="g" and player=="s"):
        return False
    elif(comp=="g" and player=="w"):
        return True
    else:
        return None                           

print("Computer Turn")
compChoice = random.randint(1,3)
if(compChoice==1):
    comp = "s"
elif(compChoice==2):
    comp = "w"
elif(compChoice==3):
    comp = "g"

player = input("Player Turn:  Snake(s), Water(w), Gun(g): ")
w = Game(comp,player)

if(w==None):
    print("It's a tie")
elif(w==True):
    print("Player wins")
elif(w==False):
    print("Computer wins")