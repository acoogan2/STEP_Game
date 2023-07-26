import random


print("WELCOME TO ROCK, PAPER, SCISSORS!")

choices = ["ROCK", "PAPER", "SCISSORS"]

while True:
    com = random.randint(0,2)
    print("ENTER YOUR CHOICE:")
    print("0.ROCK")
    print("1.PAPER")
    print("2.SCISSORS")
    opchoice = int(input("ENTER YOUR CHOICE, 1/2/3? "))
    
    if opchoice not in [1, 2, 3]:
        print("INVALID, PLEASE TRY AGAIN")
        continue
    print("YOUR CHOICE:(0. ROCK, 1. PAPER, 2. SCISSORS)" + str(opchoice))
    print("COMPUTER CHOICE(0. ROCK, 1. PAPER, 2. SCISSORS)" + str(com))
    
    
    if opchoice == com:
            print("TIE")
        
    elif(opchoice == 0 and com == 2) or (opchoice == 1 and com == 0) or (opchoice == 2 and com == 1):
            print("YOU WIN")
        
    else:
        print("YOU LOSE")
    
    playagain = input("DO YOU WANT TO PLAY AGAIN? (y/n): ")
    if playagain == "n":
        break
        

