def parse_input(user_input: str): 
    cmd, *args = user_input.split()   # split by spaces into command and arguments
    cmd = cmd.strip().lower()    # remove upper case
    return cmd, *args


def add_contact(args, contacts: dict) -> str:   # Adding a new contact to the dictionary
    name, phone = args
    contacts[name] = phone  # save or overwrite contact
    return "Contact added."


def change_contact(args, contacts: dict) -> str:   # Changing contact number
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts: dict) -> str:   # Shows a phone number after typing name
    name = args[0]  # User typed name only
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts: dict) -> str:   # Shows all contacts
    if not contacts:
        return "No contacts saved."
    result_lines = []
    for name, phone in contacts.items():
        result_lines.append(f"{name}: {phone}")
    return "\n".join(result_lines)

def main():
    contacts = {}  # creates dictionary to store contacts: {name: phone}  # example only
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Bye bye sweetheart!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)
        elif command == "all":
            result = show_all(contacts)
            print(result)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
