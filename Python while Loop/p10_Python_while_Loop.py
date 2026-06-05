#10.Write a program to keep asking the user for a password until the correct password is entered.
correct_password = "admin123"
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Password correct!")
        break
    else:
        print("Incorrect password. Try again.")