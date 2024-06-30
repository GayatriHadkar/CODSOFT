class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("No contacts found.")
        return results

    def update_contact(self, index, contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = contact

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone to search: ")
            results = manager.search_contact(search_term)
            for result in results:
                print(result)

        elif choice == '4':
            search_term = input("Enter name or phone to search for update: ")
            results = manager.search_contact(search_term)
            if len(results) == 1:
                index = manager.contacts.index(results[0])
                name = input(f"Enter new name ({results[0].name}): ") or results[0].name
                phone = input(f"Enter new phone ({results[0].phone}): ") or results[0].phone
                email = input(f"Enter new email ({results[0].email}): ") or results[0].email
                address = input(f"Enter new address ({results[0].address}): ") or results[0].address
                updated_contact = Contact(name, phone, email, address)
                manager.update_contact(index, updated_contact)
                print("Contact updated successfully!")
            else:
                print("Multiple or no contacts found. Please refine your search.")

        elif choice == '5':
            search_term = input("Enter name or phone to search for deletion: ")
            results = manager.search_contact(search_term)
            if len(results) == 1:
                index = manager.contacts.index(results[0])
                manager.delete_contact(index)
                print("Contact deleted successfully!")
            else:
                print("Multiple or no contacts found. Please refine your search.")

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
