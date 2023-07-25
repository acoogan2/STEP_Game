counter = 0
import random
number = random.randint(1, 100)
name = input("Enter your name")
print("Welcome to guess the number" + name)
print("How many tries will it take you to guess the number?")
while True:
    guess = int(input("Enter a guess"))
    if guess == number:
        counter=+1
        print(str"Correct! It took you" + counter +"guesses to get the correct number.")
        break 
    elif number < guess:
        print("TOO HIGH")
        counter+=1
    elif number > guess:
        print("TOO LOW")
        counter+=1
    else:
        print("ERROR")
       
        
        

