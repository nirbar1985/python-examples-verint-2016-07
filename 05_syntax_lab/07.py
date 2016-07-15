"""
Write a program that selects random number between 1 and 100. 
The user must guess the number selected and after each guess to print Bigger or Smaller Too Too by the ratio of the number selected guess.


"""
from random import randint

num = randint(1, 100)

while (True):
	user_guess = int(raw_input("Type your number: "))
	
	if(user_guess == num):
		print "You succeed, the num is %d", num
		break
	elif(user_guess >  num):
		print "too big"
	else:
		print "too small"
