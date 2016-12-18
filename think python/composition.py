# 
# Given the radius calculates area
def area(radius):
	from math import pi
	tmp = pi * radius**2
	return tmp
	
# The following function computes the distance of two given points
def distance(x1,y1,x2,y2):
	from math import sqrt
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	distance = sqrt(dsquared)
	return distance
	
def circle_area(xc,yc,xp,yp):
	return area(distance(xc,yc,xp,yp))
	
print circle_area(0,0,3,4)