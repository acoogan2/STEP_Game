num1 = int(input("Enter your first number"))
operator = input("enter the operation +,-, /, *")
num2 = int(input("Enter your second number"))

if operator == "+":
	print(num1 + num2)

elif operator == "-":
	print(num1 - num2)

elif operator == "*":
	print(num1 * num2)

elif operator == "/":
	if(num2==0):
		print("cant divide by 0")
	else:	
		print(num1 / num2)

else:
	print ("invalid operator. Please try again") 