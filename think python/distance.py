#Incremental develoment 
# The following function computes the distance of two given points
def distance(x1,y1,x2,y2):
	from math import sqrt
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	distance = sqrt(dsquared)
	return distance
	
print distance(0,0,2,2)
 