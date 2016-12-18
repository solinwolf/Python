# condition statement 
# functionality: check whether the input is integer or not.If the input is integer,
# 				 is it positive or negetive or zero
def condition(n):
	tmp=int(n)
	if tmp>0:
		print '%d is positive'%tmp
	elif tmp==0:
		print '%d is zero'%tmp
	else :
		print '%d is negetive'%tmp

while True:
	n = raw_input("Input an integer:")
	if n=='done':
		break
	condition(n)