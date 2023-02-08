phonebook = {}

def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact {name} added with number {number}")

def find_contact(name):
    if name in phonebook:
        print(f"{name}'s number: {phonebook[name]}")
    else:
        print(f"{name} not found in phonebook")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted from phonebook")
    else:
        print(f"{name} not found in phonebook")

print("Welcome to the phonebook application")
while True:
    print("1. Find phone number")
    print("2. Insert a phone number")
    print("3. Delete a person from the phonebook")
    print("4. Terminate")
    choice = int(input("Select operation on Phonebook App (1/2/3): "))
    if choice == 1:
        name = input("Enter name to find: ")
        find_contact(name)
    elif choice == 2:
        name = input("Enter name: ")
        number = input("Enter number: ")
        if number.isdigit():
            add_contact(name, number)
        else:
            print("Invalid input format, cancelling operation...")
    elif choice == 3:
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == 4:
        break
    else:
        print("Invalid option selected. Try again.")

print("Exiting Phonebook App")