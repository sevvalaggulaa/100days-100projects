# Welcome Message Generator
from datetime import datetime
#Step 1: Ask for user details
name = input("What is your name? ").title()
surname = input("What is your surname? ").uppera()
hobby = input("What is your favorite hobby? ").lower()
color = input("What is your favorite color? ").lower()

#Step 2: Generate a personalized welcome message
current_date=datetime.now().strftime("%d-%m-%Y")
print("\n--- Welcome Message ---")
print(f"Date: {current_date}")
print(f"Hello, {name} {surname}")
print(f"Welcome to the world of Python programming.")
print(f"It is great to know that you love {hobby} and your favorite color is {color}.")
print(f"Get ready to build something amazing today.")
