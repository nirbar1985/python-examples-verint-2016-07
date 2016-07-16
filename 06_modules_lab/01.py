"""

write a program that recieves in argv a number and prints 
that number of times- "Hello Python" 


"""

import sys

num = int(sys.argv[1])

for _ in range(num):
	print "Hello Python"