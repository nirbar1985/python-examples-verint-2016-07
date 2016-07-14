"""

write program that calculates randomly numbers between 1 to 1,000,000 until it finds 
number that divides with 7,13,15.


"""
while(True):

	from random import randint
	num = randint(1, 10000)

	if((num%7 == 0) & (num%13 == 0) & (num%15 == 0)):
		break

print num
