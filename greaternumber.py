num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
while True:
    if num1 == num2:
        print("numbers are equal")
        break
    elif num1 > num2:
        print(num1)
        break
    elif num1 < num2:
        print(num2)
        break
    else:
        print("ERROR")
        break