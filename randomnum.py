number = 35
# number can be changed

userInput = int(input("Pick a number "))
if userInput == number:
	print ("good job")	
while userInput != number:
	if int(userInput) < number: 
		print ("guess higher")
	if int(userInput) > number: 
		print ("Oops! Guess lower")
	if int(userInput)== number: 
		print ("good job")	
		break
	userInput = int(input("try again "))
