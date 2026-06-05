#2.	Write a program to check whether a number is even or odd. 

num = int(input("Enter a number: "))

if num % 2 == 0:
	print("Number is even.")
elif num % 2 == 1:
	print("Number is odd.")
else:
	print("Number is zero.")

