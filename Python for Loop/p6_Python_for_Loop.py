#6.	Write a program to print the multiplication table of a given number. 
n = int(input("Enter a number: "))
print("Multiplication Table of", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
    