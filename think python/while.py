#while statement

def countdown(n):
	while n>0:
		print n
		n=n-1
	print 'Blastoff'

countdown(10)
#Flow of execution for a while statement 
# 1.Evaluate the condition,yielding True or False
# 2.If the condition is False,exit the while statement and continue the next statement 
# 3.If the condition is True,execute the body and then go back to step 1
