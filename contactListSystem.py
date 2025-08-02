contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def display_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

while True:
    choice = input("Add/View/Quit: ").lower()
    if choice == 'add':
        name = input("Name: ")
        phone = input("Phone: ")
        add_contact(name, phone)
    elif choice == 'view':
        display_contacts()
    elif choice == 'quit':
        break
