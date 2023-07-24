name = "Alice"
print("hi " + name)
print("duck slippers")
print("hello" + name)
age = 13
print(age)
name = "andrea"
print(name)
num1 =73
num2 =54
print(num1 + num2)
print(num1 / num2)
print (num1 - num2)
friendsname = input("andrea")
print(friendsname)


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


