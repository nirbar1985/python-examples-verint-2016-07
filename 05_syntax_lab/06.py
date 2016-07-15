"""

write program that raffles 2 numbers between 1-10 , and calculates the smallest mutual divider of both. for example 4 and 6 the answer is 12  


"""
from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)

i=0

while(i != num1*num2):

	i += num1
	if(i%num2==0):
		break
print i
		
		
		