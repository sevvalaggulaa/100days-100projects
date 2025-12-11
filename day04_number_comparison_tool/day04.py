#Number Comparison Tool
#Step 1: Get user input for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

#Step 2: Compare the first two numbers 
print("\n--- Comparison Results ---")

if number1 > number2:
  print(f"{number1} is greater than {number2}")
elif number1 == number2:
  print(f"{number1} is equal to {number2}")
else:
  print(f"{number1} is less than {number2}")

#Step 3: Check if any number is zero
if number1 == 0 or number2 == 0 or number3 == 0:
  print("At least one number is zero")
else:
  print("Both numbers are non-zero")

#Step 4: Compare all three numbers
print("\n--- All Comparison Results ---")
if number1 == number2 == number3:
  print("All three numbers are equal. ")
else:
  largest = max(number1, number2, number3)
  smallest = min(number1, number2, number3)
  print(f"The largest number is {largest}")
  print(f"The smallest number is {smallest}")

#Step 5: Check positive/negative/zero for each number
print("\n--- Number Sign Check ---")
def check_sign(n,name):
  if n > 0:
    print(f"{name} is positive.")
  elif n == 0:
    print(f"{name} is zero.")
  else:
    print(f"{name} is negative.")
  
check_sign(number1, "Number 1")
check_sign(number2, "Number 2")
check_sign(number3, "Number 3")
