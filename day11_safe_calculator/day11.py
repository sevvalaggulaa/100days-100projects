# Safe Calculator

from datetime import datetime
LOG_FILE = "calculator_errors.log"

# Step 1: Define Calculator Functions
def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  if y==0:
    raise ZeroDivisionError("Cannot divide by zero")
  return x/y
def modulus(x,y):
  if y==0:
    raise ZeroDivisionError("Cannot modulus by zero")
  return x%y
def exponent(x,y):
  return x**y

def log_error(error_type: str, message: str):
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open(LOG_FILE, "a") as file:
    file.write(f"[{timestamp}] {error_type}: {message}\n")

#Step 2: Display Menu
def show_menu():
  print("\n\nSelect an operation: ")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Modulus")
  print("6. Exponent")
  print("7. Exit")

#Step 3: Main Program
while True:
  show_menu()
  choice = input("Enter your choice (1-7): ")

  if choice == "7":
    print("Exiting the calculator. Goodbye! ")
    break

  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if choice == "1":
      print("Result: ", add(num1,num2))
    elif choice == "2":
      print("Result: ", subtract(num1,num2))
    elif choice == "3":
      print("Result: ", multiply(num1,num2))
    elif choice == "4":
      print("Result: ", divide(num1,num2))
    elif choice == "5":
      print("Result: ", modulus(num1,num2))
    elif choice == "6":
      print("Result: ", exponent(num1,num2))
    else:
      print("Invalid choice. Please select a number between 1 and 7.")

  except ValueError as e:
    print("Invalid input. Please enter valid numbers.")
    log_error("Invalid Input", str(e))
  except ZeroDivisionError as e:
    print(f"Error: {e}")
    log_error("Zero Division Error", str(e))
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    log_error("Unexpected Error", str(e))
  finally:
    print("Thank you for using the calculator!..")
    
