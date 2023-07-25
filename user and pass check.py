counter - 3
defpass - "1234"
defusername - "abc"
while True:
	Username - input("Enter username")
	Password - input("Enter Password")
	if Username == defusername and Password == defpass:
		print("Access Granted")
	Else:
		print(Access Denied. Tries left")
		counter-=1
		print(counter)
