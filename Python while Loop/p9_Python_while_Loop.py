#9.	Write a program to find the factorial of a given number using a while loop.
num = int(input("Enter a number: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print("Factorial:", factorial)
