#3.	Write a program to find the greater number between two numbers. 

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 1st number: "))

if n1 > n2:
	print(n1,"is greater.")
elif n1 < n2:
	print(n2,"is greater.")
else:
	print(n1," & ",n2," are equal numbers.")