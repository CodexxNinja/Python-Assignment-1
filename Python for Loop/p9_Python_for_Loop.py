#9.	Write a program to find the factorial of a given number using a for loop. 

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial of", num, "is", factorial)