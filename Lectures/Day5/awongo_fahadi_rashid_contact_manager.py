# contact management system
contacts = []
global name, phone_number
def add_contact(name, phone_number, email):
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    if search_contact(name):
        print("Contact already exists.")
        return
    elif not name or not phone_number or not email:
        print("All fields are required.")
        return
    elif not phone_number.isdigit():
        print("Phone number must contain only digits.")
        return
    elif len(phone_number) != 10:
        print("Phone number must be 10 digits long.")
        return
    elif '@' not in email or '.' not in email:
        print("Invalid email address.")
        return
    else:
        contacts.append({"name": name, "phone_number": phone_number, "email": email})

def display_contacts():
    for contact in contacts:
        if contacts == []:
            print("No contacts found.")
            return
        else:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact['email']}")
def search_contact(keyword):
    for contact in contacts:
        if contact['name'].lower() == keyword.lower():
            return contact
        elif contact['phone_number'] == keyword:
            return contact
        elif contact['email'].lower() == keyword.lower():
            return contact
        else:
            print("Contact not found.")
    return None
def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
def edit_contact(name, new_name, new_phone_number, new_email):
    contact = search_contact(name)
    if contact:
        if new_name:
            contact['name'] = new_name
        if new_phone_number:
            if not new_phone_number.isdigit():
                print("Phone number must contain only digits.")
                return
            elif len(new_phone_number) != 10:
                print("Phone number must be 10 digits long.")
                return
            contact['phone_number'] = new_phone_number
        if new_email:
            if '@' not in new_email or '.' not in new_email:
                print("Invalid email address.")
                return
            contact['email'] = new_email
    else:
        print("Contact not found.")
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Edit Contact")
        print("4. Search Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(name = None, phone_number = None, email = None)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            name = input("Enter contact name to edit: ")
            new_name = input("Enter new name (or press Enter to keep current): ")
            new_phone_number = input("Enter new phone number (or press Enter to keep current): ")
            new_email = input("Enter new email (or press Enter to keep current): ")
            edit_contact(name, new_name, new_phone_number, new_email)
        elif choice == '4':
            name = input("Enter contact name to search: ")
            contact = search_contact(name)
            if contact:
                print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact['email']}")
            else:
                print("Contact not found.")
        elif choice == '5':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
            print("Contact deleted if it existed.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":    main()
