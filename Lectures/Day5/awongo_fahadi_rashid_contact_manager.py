# contact management system
contacts = []
global name, phone_number
def add_contact(name, phone_number):
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    if search_contact(name):
        print("Contact already exists.")
        return
    elif not name or not phone_number:
        print("Name and phone number cannot be empty.")
        return
    elif not phone_number.isdigit():
        print("Phone number must contain only digits.")
        return
    elif len(phone_number) != 10:
        print("Phone number must be 10 digits long.")
        return
    else:
        contacts.append({"name": name, "phone_number": phone_number})

def display_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}")
def search_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return None
def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(name = None, phone_number = None)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact = search_contact(name)
            if contact:
                print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}")
            else:
                print("Contact not found.")
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
            print("Contact deleted if it existed.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":    main()
