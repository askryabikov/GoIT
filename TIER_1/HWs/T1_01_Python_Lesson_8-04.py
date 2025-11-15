# Base version was taken from Home task 6-4

def input_error(func):       # decorator to handle user input errors
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:   # in case not enough arguments for add/change
            return "Give me name and phone please."
        except KeyError:     # contact not found in dictionary
            return "Contact not found."
        except IndexError:   # no name provided 
            return "Enter the argument for the command."
    return inner


def parse_input(user_input: str):
    cmd, *args = user_input.split()   # split by spaces into command and arguments
    cmd = cmd.strip().lower()         # remove upper case
    return cmd, *args


@input_error
def add_contact(args, contacts: dict) -> str:   # Adding a new contact to the dictionary
    name, phone = args                # exactly 2 arguments or ValueError
    contacts[name] = phone            # saves or overwrites contact
    return "Contact added."


@input_error
def change_contact(args, contacts: dict) -> str:   # Changing contact number
    name, phone = args                # exactly 2 arguments or ValueError
    if name not in contacts:          # let decorator handle "not found"
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts: dict) -> str:   # Shows a phone number after typing name
    name = args[0]                    # IndexError if nothing in args
    return contacts[name]             # KeyError if name not in contacts


@input_error                          # Additional
def show_all(contacts: dict) -> str:  # Shows all contacts
    if not contacts:
        return "No contacts saved."
    result_lines = []
    for name, phone in contacts.items():
        result_lines.append(f"{name}: {phone}")
    return "\n".join(result_lines)


def main():
    contacts = {}                      # creates dictionary to store contacts: {name: phone}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)   # unpack command and arguments
        if command in ["close", "exit"]:
            print("Good bye Sweetheart!")
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
