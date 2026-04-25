def calculate_circumference(radius):
    return 2 * 3.14 * radius

r = float(input("Enter the radius: "))
result = calculate_circumference(r)

print("The circumference is:", result)