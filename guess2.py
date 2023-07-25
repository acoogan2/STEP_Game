counter = 0
low = 1
high = 100
mid = (low + high)/2
import random
number = random.randint(1, 100)
while True:
    if number == mid:
       print("Correct")
       print("You guessed the number in")
       print(counter+"tries")
       counter+=1
       break
    elif number < mid:
        low = mid + 1
        counter+=1
        mid=(low + high)/2
    else:
        low = mid+1
        mid = (low+high)/2
        counter+=1
            


