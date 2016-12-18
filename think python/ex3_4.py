#Exercise3.4
def do_twice(f,para):
	f(para)
	f(para)
	
def do_four(f,para):
	do_twice(f,para)
	do_twice(f,para)	
	
def print_funct(para):
	print para
	
do_four(print_funct,"Solin")



