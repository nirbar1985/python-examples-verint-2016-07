"""
write a program eivh gets in argv 2 numbers and prints its sum



"""

import sys

if len(sys.argv) != 3:
	sys.exit("please enter exactly 2 parameters")

try:
	num1 = int(sys.argv[1])
	num2 = int(sys.argv[2])

except:
	sys.exit("please enter only numbers as parameters")
		

print sum((num1,num2))