start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

even_squares = []
odd_squares = []

for i in range(start, end + 1):
    square = i * i
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("Even squares:", even_squares)
print("Odd squares:", odd_squares)