# recursion 
# functionality: recursively display numbers 0-n

def countdown(n):
	if n<0:
		print '%d is not positive'%n 
		return 
	if n==0:
		print 'Blastoff'
	else:
		print n
		countdown(n-1)
	return 

countdown('pw')
