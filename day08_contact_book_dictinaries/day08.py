# Contact Book

# Step 1: Initialize an empty contact book
contacts = {}

# Step 2: Display the menu
def show_menu():
    print("\n---- Contact Book Menu ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Quit")

# Step 3: Add a contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    email = input("Enter contact email: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact {name} has been added successfully.")

# Step 4: View all contacts
def view_contacts():
    if contacts:
        print("\n---- Contact List ----")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print("----------------------")
    else:
        print("Your contact book is empty.")

# Step 5: Search a contact
def search_contact():
    name = input("Enter the name of the contact you want to search: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print(f"Contact {name} not found.")

# Step 6: Edit a contact
def edit_contact():
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email
        print(f"Contact {name} has been updated successfully.")
    else:
        print(f"Contact {name} not found.")

# Step 7: Delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted successfully.")
    else:
        print(f"Contact {name} not found.")

# Step 8: Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).")

