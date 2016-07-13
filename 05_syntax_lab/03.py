"""

write program that gets a random number between 1-10,000 and calculates the sum of its digits


"""


from random import randint
num = randint(1, 10000)

list_of_ints = [int(i) for i in str(num)]
sum = 0
for i in range (0,len(list_of_ints)):
	sum +=  list_of_ints[i]
	
print sum	
