#10. Write a program to check whether a number is within the range of 1 to 100.
num = int(input("Enter a number: "))

if 1 <= num <= 100:
    print(num, "is within the range of 1 to 100.")
else:
    print(num, "is not within the range of 1 to 100.")