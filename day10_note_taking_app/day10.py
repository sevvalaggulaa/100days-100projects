#Note-Taking App

import datetime
import os 

#Step 1: Define file name
FILE_NAME = "myNotes.txt"

#Step 2: Display menu options
def show_menu():
    print("\n--- Note-Taking App Menu ---")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

#Step 3: Add a new note 
def add_note():
    note = input("Enter your note: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    note = f"{timestamp} - {note}"
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")
  
#Step 4: View all notes
def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
          content = file.read()
          if content:
            print("\n--- Your Notes ---")
            print(content)
          else:
            print("\nNo notes found.")
    except FileNotFoundError:
        print("No notes found.")
    
#Step 5: Delete all notes
def delete_notes():
  confirm = input("Are you sure you want to delete all notes? (yes/no): ")
  if confirm.lower() == "yes":
    with open(FILE_NAME, "w") as file:
      pass 
    print("All notes deleted successfully!")
  else:
    print("Deletion canceled.")

#Step 6: Main Program Loop 
while True:
  show_menu()
  choice = input("Enter your choice (1/2/3/4): ")

  if choice == "1":
    add_note()
  elif choice == "2":
    view_notes()
  elif choice == "3":
    delete_notes()
  elif choice == "4":
    print("Exiting the Note-Taking App. Goodbye!")
    break 
  else:

    print("Invalid choice. Please try again.")
