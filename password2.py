counter = 3
defpass = "1234"
defusername = "abc"
while True:
	username = input("ENTER USERNAME")
	password = input("ENTER PASSWORD")
	if defusername == username and defpass == password:
		print("ACCESS GRANTED")
		print("HELLO OPERATOR")
		print("WELCOME TO CALCULATOR")
		num1 = int(input("ENTER YOUR FIRST NUMBER"))
		operator = input("ENTER THE OPERATION +,-, /, *")
		num2 = int(input("ENTER YOUR SECOND NUMBER"))

		if operator == "+":
			print(num1 + num2)
			break

		elif operator == "-":
			print(num1 - num2)
			break

		elif operator == "*":
			print(num1 * num2)
			break

		elif operator == "/":
			if(num2==0):
				print("Error")
			else:	
				print(num1 / num2)
				break

		else:
			print ("ERROR. PLEASE TRY AGAIN") 
			break
			break
	else:
		print("ACCESS DENIED. TRIES LEFT")
		print(counter)
		counter-=1
		if counter == -1:
			print("USER BLOCKED")
			break	

	
		



