# return statement 
# Given the radius calculates area
def area(radius):
	from math import pi
	tmp = math.pi * radius**2
	return tmp
	
# Computes absolute value
def absolute_value(val):
	if val<0:
		return -val
	else:
		return val


print area(2)
print absolute_value(-100.10)
