while True:
	print("1.NO OF WORDS AND DISPLAY EACH WORD")
	print("2.COUNT OF VOWELS AND WORDS STARTING WITH VOWELS")
	print("3.REVERSE THE STRING WITH INDEXING")
	print("4.DISPLAY WORDS INDIVIDUALLY AND STORE PALINDROME WORDS IN A LIST")
	c=int(input("Enter your choice"))
	if c==1:
		a=input("Enter your string")
		b=a.split(" ")
		print("No of words in the string entered : ",len(b))
		x=[]
		for i in b:
			if i not in x:
				x.append(i)
		for j in x:
			d=b.count(j)
			print(j,"::No of times repeated::",d)
	elif c==2:
		a=input("Enter your string")
		b=['a','e','i','o','u','A','E','I','O','U']
		x=a.split(" ")
		count=0
		for i in a:
			if (i in b):
				count=count+1
		print("Number of vowels in the string entered",count)
		for j in x:
			for k in b:
				if j[0]==k:
					print(j,"starts with a vowel")
	elif c==3:
		a=input("Enter your string")
		d=0
		for j in a:
			d=d+1
		rev=""
		for i in range(-1,-(d+1),-1):
			x=a[i]
			rev=rev+x
		print(rev)
	elif c==4:
		a=input("Enter your string")
		b=a.split(" ")
		l=list()
		for i in b:
			print("The seperated value",i)
			rev=""
			d=len(i)
			for j in range(-1,-(d+1),-1):
				k=i[j]
				rev=rev+k
				if rev==i:
					l.append(rev)
		print(l,"is palindrome")
	else:
		print("invalid")
	ch=input("Do you want to continue")
	if ch =="yes":
		continue
	else:
		break
