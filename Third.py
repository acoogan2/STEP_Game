counter = 5
default = "1234"
while True:
	password1= input("enter password")
	if default==password1:
		print("Welcome User")
		break 
	else:
		print("Password incorrect, please try again. Tries left =")
		print("counter")
		counter-=1
		if counter==0:
			print("User Blocked")
			break



