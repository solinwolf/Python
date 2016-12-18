
#definition of a new function void function
def funct(para):
	name = raw_input("Input :")
	print "parameter is '",para,"'"
	print "Local variable :",name
	
#llegle function call
#funct("This is testing of function") 

#illegle use of a local variable
#print name	 
	
#fruitful function is a function that yields results;
def fruitful_funct(para):
	print "Local function!Parameter is : ",para,"And now returning it back"
	return para
	
result = fruitful_funct("fruitful function")
print "Getting result of :",result