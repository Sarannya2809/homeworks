decimal_num = int(input("Enter a decimal number: "))
binary_num = ""

if decimal_num == 0:
    binary_num = "0"
else:
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2

print("Binary version:", binary_num)