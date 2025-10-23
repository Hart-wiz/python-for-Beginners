# Mini Project: Contact Book CLI

# Description

# Create a simple Command-Line Contact Book where users can:
# Add, view, search, update, and delete contacts
# Store contact details using a dictionary
# Loop until the user exits

# ----------------------------------------------------------------------------

print("=== Contact Book CLI ===")

contacts = {}

while True:
    print("\nOptions: add | view | search | delete | exit")
    choice = input("Enter choice: ").lower()

    if choice == "add":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"✅ {name} added successfully!")

    elif choice == "view":
        if not contacts:
            print("No contacts available.")
        else:
            for name, info in contacts.items():
                print(f"{name} - {info['phone']} - {info['email']}")

    elif choice == "search":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]['phone']}, {contacts[name]['email']}")
        else:
            print("❌ Contact not found.")

    elif choice == "delete":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"🗑️ {name} deleted.")
        else:
            print("❌ Contact not found.")

    elif choice == "exit":
        print("👋 Goodbye!")
        break

    else:
        print("Invalid option. Try again.")





# ==========================================================================
# Try It Yourself

# Save contacts to a file (contacts.txt) and load them on startup.

# Add an update option for editing contact info.

# Show the total number of saved contacts.