"""

write program that reads from the user lines until he enters an empty line.
afterwards the program will print all the lines written backwards.


"""

word_count = 0
line = raw_input()

lines =list()
while len(line) > 0:
    #word_count += len(line.split())
	lines.append(line)
	line = raw_input()

lines.reverse()
print lines