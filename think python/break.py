# break statement 
# Take input from the user until they type done 
while True:
	line = raw_input('>')
	if line == 'done':
		break
	print line
print 'Done'
# Flow of execution for a break statement 
# 1.take input from the user and store in the variable named  line 
# 2.Evaluate the condition statement (if) ,yielding True or False 
# 3.If 2. yields True (line == 'done') jump out of the while statement and then print 'Done'. If 2. returns False (line != 'done') print lline

