n=int(input("Enter the number"))
if n==0:
	print(0)
elif n==1:
	print(1)
else:
	a=0
	b=1
	print(a)
	print(b)
for i in range(n-2):
	fib=a+b
	print(fib)
	a=b
	b=fib
	