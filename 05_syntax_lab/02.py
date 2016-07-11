"""

write program that gets randonly 7 numbers and prits its sum. if it divides with 7 need to print "boom" as well.


"""


from random import randint

sum=0

for i in range (1,11):

	sum +=randint(1, 100)
print sum

if(sum%7 == 0):
	print "boom"
