#Ingredients Checker

#Step 1: Define the recipe ingredients
recipe_ingredients = {"flour","sugar","butter","eggs","milk"}

#Step 2: Get user input for available ingredients
user_input=input("Enter the ingredients you have (seperated by commas): ")
user_ingredienst = set(user_input.split(", "))

#Step 3: Compare Ingredients
missing_ingredients = recipe_ingredients - user_ingredienst
extra_ingredients = user_ingredienst - recipe_ingredients

#Step 4: Display Results
print("\n--- Ingredients Check Results ---")
if missing_ingredients:
  print(f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
  print("You have all the ingredients needed.")

if extra_ingredients:
  print(f"You have extra ingredients: {', '.join(extra_ingredients)}")
else: 
  print("You have all the ingredients needed.")
