#Shopping List App

#Step 1: Initialize an empty shopping list
shopping_list = []

#Step 2: Define the main menu 
def show_menu():
  print("\n--- Shopping List Menu ---")
  print("1. View the shipping list")
  print("2. Add an item")
  print("3. Remove an item")
  print("4. Clear the list")
  print("5. Edit an item")
  print("6. Quit")

#Step 3: Main Program Loop 
while True:
  show_menu()
  choice = input ("Enter your choice (1-5): ")

  if choice == "1":
    print("\n--- Shopping List ---")
    if not shopping_list:
      print("Your shopping list is empty.")
    else:
      for index, item in enumerate(shopping_list):
        print(f"{index + 1}. {item}")
  elif choice == "2":
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")
  elif choice == "3":
    item = input("Enter the item to remove: ")
    if item in shopping_list:
      shopping_list.remove(item)
      print(f"{item} has been removed from the shopping list.")
    else:
      print(f"{item} is not in the shopping list.")
  elif choice == "4":
    shopping_list.clear()
    print("The shopping list has been cleared.")
  elif choice == "5":
    if not shopping_list:
      print("The shopping list is empty. Nothing to edit.")
    else:
      for i, item in enumerate(shopping_list):
        print(f"{i + 1}. {item}")
      try:
        index = int(input("Enter the item number to edit: ")) -1
        if 0 <= index <= len(shopping_list):
          new_value = input("Enter the new item: ") 
          old_value = shopping_list[index]
          shopping_list[index] = new_value 
          print(f"{old_value} has been replaced with {new_value} in the shopping list.")
        else:
          print("Invalid item number. Please try again.")
      except ValueError:
        print("Invalid input. Please enter a number.")


  elif choice == "6":
    with open ("shopping_list.txt", "w") as file:
      for item in shopping_list:
        file.write(item + "\n")
    print("Exiting the program. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")


