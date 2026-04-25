age = int(input("Enter your age: "))

if age < 0:
    print("Error: Age cannot be negative.")
else:
    if age % 2 == 0:
        print("The age is even.")
    else:
        print("The age is odd.")