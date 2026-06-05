#7.	Write a program to count the number of digits in a given number using a while loop.
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)