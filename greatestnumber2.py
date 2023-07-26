num1 = int(input("ENTER NUMBER 1: "))
num2 = int(input("ENTER NUMBER 2: "))
num3 = int(input("ENTER NUMBER 3: "))
while True:
    if num1 == num2 and num2 == num3 and num3 == num1:
        print("NUMBERS ARE EQUAL")
        break
    elif num1 > num2 and num1 > num3 and num2 > num3:
        print("GREATEST: " + str(num1))
        print("MIDDLE: " + str(num2))
        print("LEAST: " + str(num3))
        break
    elif num1 > num2 and num1 > num3 and num2 < num3:
        print("GREATEST:" + str(num1))
        print("MIDDLE: " + str(num3))
        print("LEAST: " + str(num2))
        break
    elif num1 < num2 and num3 < num2 and num1 > num3:
        print("GREATEST: " + str(num2))
        print("MIDDLE: " + str(num1))
        print("LEAST: " + str(num3))
        break
    elif num1 < num2 and num3 < num2 and num1 < num3:
        print("GREATEST: " + str(num2))
        print("MIDDLE: " + str(num3))
        print("LEAST: " + str(num1))
        break
    elif num1 < num3 and num3 > num2 and num1 > num2:
        print("GREATEST: " + str(num3))
        print("MIDDLE: " + str(num1))
        print("LEAST: " + str(num2))
        break
    elif num1 < num3 and num3 > num2 and num1 < num2:
        print("GREATEST: " + str(num3))
        print("MIDDLE: " + str(num2))
        print("LEAST: " + str(num1))
        break
    else:
        print("ERROR")
        break