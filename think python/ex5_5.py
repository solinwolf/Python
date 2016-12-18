# Exercise5.5 
# Read the following function and try to figure out what it does
def draw(t,length,n):
	if n==0:
		return 
	angle = 50
	fd(t,length*n)
	lt(t,angle)
	draw(t,length,n-1)
	rt(t,2*length)
	draw(t,length,n-1)
	lt(t,angle)
	bk(t,length*n)

	
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob
draw(bob,10,10)
wait_for_user()