def op(a,b,o):
	if o=='+':
		return a+b
	if o=='-':
		return a-b
	if o=='*':
		return a*b
	if o=='/':
		return a/b
def ano(c):
	a=int(input("Enter a num : "))
	o=str(input("Enter a operator : "))
	return op(c,a,o)


i=1

a=int(input("Enter a num : "))
o=str(input("Enter a operator : "))
b=int(input("Enter a num : "))
c=op(a,b,o)
print("result : ",c)
while i==1:
	print("do you want to continue :(1 or 0)")
	i=int(input())
	if i==1:
		s=ano(c)
		print(s)
		c=s
	else:
		break




