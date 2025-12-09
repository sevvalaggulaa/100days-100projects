from datetime import datetime

#Personalized Greeting Program

#Step1: Ask for user details
name=input("What is your name? ").title()
birth_year = int(input("Which year were you born? "))
color = input("What is your favorite color? ").lower()
current_year = datetime.now().year
count_age = current_year- birth_year

#Step2: Generate a personalized greeting message
print("\n---- Personalized Greeting ----")
print(f"Hello {name}!")
print(f"You are {count_age} years old and {color} is a beautiful color! ")
print("You're now ready to start your Python adventure")
