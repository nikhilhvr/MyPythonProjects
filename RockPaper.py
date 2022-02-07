import random

userWin = 0
ComputerWin = 0
options = ["rock","paper","sessior"]

while True:
    userPick = input("Type one of rock/paper/sessior or q for Quit ")
    if userPick == "q":
        break
    
    if userPick not in options :
        continue
    
    randomNumber = random.randint(0, 2)

    computerPick = options[randomNumber]
    print("Computer picked",computerPick)

    if userPick == "sessior" and computerPick == "paper":
        print("you won!")
        userWin += 1
    elif userPick == "rock" and computerPick == "sessior":
        print("you won!")
        userWin += 1
    elif userPick == "paper" and computerPick == "rock":
        print("you won!")
        userWin += 1     
    elif userPick == "paper" and computerPick == "paper":
        print("Nobody won and Nobody cares!")  
    elif userPick == "rock" and computerPick == "rock":
        print("Nobody won and Nobody cares!") 
    elif userPick == "sessior" and computerPick == "sessior":
        print("Nobody won and Nobody cares!")        
    else :
        print("Computer won!")

print ("you won", userWin, "times.")
print("Computer", ComputerWin, "times.")
print("Game is over now. Bie bie!! :)")
