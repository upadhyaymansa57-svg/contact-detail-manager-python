contacts = {}

while True:
    print("\n1. Add")
    print("2. Search")
    print("3. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif ch == '2':
        name = input("Enter name to search: ")
        print(contacts.get(name, "Not found"))

    elif ch == '3':
        break

    else:
        print("Invalid choice")
