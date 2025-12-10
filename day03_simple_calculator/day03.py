# Simple Calculator

# Step 1: Get user input for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Step 2: Choose the operation
print("Choose the operation: +  -  *  /  ^  %")
operation = input("Operation: ")

# Step 3: Perform and display the result
print("\n---- Calculator Results ----\n")

if operation == "+":
    print(f"{number1} + {number2} = {number1 + number2}")

elif operation == "-":
    print(f"{number1} - {number2} = {number1 - number2}")

elif operation == "*":
    print(f"{number1} * {number2} = {number1 * number2}")

elif operation == "/":
    if number2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        print(f"{number1} / {number2} = {number1 / number2}")

elif operation == "^":
    print(f"{number1} ^ {number2} = {number1 ** number2}")

elif operation == "%":
    if number2 == 0:
        print("Error: Modulus by zero is not allowed!")
    else:
        print(f"{number1} % {number2} = {number1 % number2}")

else:
    print("Invalid operation! Please choose +, -, *, /, ^ or %.")

