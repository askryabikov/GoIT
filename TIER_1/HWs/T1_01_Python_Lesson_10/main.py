from collections import UserDict
from datetime import datetime, date, timedelta   # for Birthday and upcoming birthdays

# PART I - FUNCTIONS

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
def add_contact(args, book) -> str:
    """Add new contact or new phone to existing contact in AddressBook."""
    if len(args) < 2:
        # will be caught by decorator as ValueError
        raise ValueError

    name = args[0]
    phone = args[1]

    # find existing record or create new one
    record = book.find(name)
    if record is None:
        record = Record(name)     # create new contact
        book.add_record(record)   # save to AddressBook

    record.add_phone(phone)       # add phone to this contact
    return "Contact added."


@input_error
def change_contact(args, book) -> str:
    """Change first phone of contact to new phone."""
    if len(args) < 2:
        raise ValueError

    name = args[0]
    new_phone = args[1]

    record = book.find(name)
    if record is None:
        # decorator will turn this into "Contact not found."
        raise KeyError

    if not record.phones:
        # if no phones yet -> just add new
        record.add_phone(new_phone)
    else:
        # change first phone in list
        old_phone_value = record.phones[0].value
        record.edit_phone(old_phone_value, new_phone)

    return "Contact updated."


@input_error
def show_phone(args, book) -> str:  # Shows all phones for given contact name
    if len(args) < 1:     # Counts arguments
        raise IndexError

    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError

    if not record.phones:
        return "No phones for this contact."

    return "; ".join(phone.value for phone in record.phones) # Join numbers with ;


@input_error
def show_all(book) -> str:    # Show all contacts in AddressBook
    if not book.data:
        return "No contacts saved."

    lines = []
    for record in book.data.values():
        # use __str__ from Record (name, phones, birthday)
        lines.append(str(record))
    return "\n".join(lines)



def main():
    book = AddressBook()                      # use AddressBook instead of plain dict
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
            result = add_contact(args, book)
            print(result)
        elif command == "change":
            result = change_contact(args, book)
            print(result)
        elif command == "phone":
            result = show_phone(args, book)
            print(result)
        elif command == "all":
            result = show_all(book)
            print(result)
        else:
            print("Invalid command.")




# PART II - CLASSES

class Field:              # Base class for all record fields
    def __init__(self, value):
        self.value = value
    def __str__(self) -> str:
        return str(self.value)


class Name(Field):        # Mandatory field
    pass


class Phone(Field):       # Phone field with 10 digits validation
    def __init__(self, value: str):
        if not self._is_valid(value):    # In case of incorrect input
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)          # 

    @staticmethod
    def _is_valid(value: str) -> bool:   # Exactly 10 digits
        return value.isdigit() and len(value) == 10
    
    
class Birthday(Field):          # Birthday field with date validation (DD.MM.YYYY)
    def __init__(self, value: str):
        try:                    # convert string into format DD.MM.YYYY
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:      # raise error if format is incorrect
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(birthday_date)

    def __str__(self) -> str:   # print birthday in DD.MM.YYYY format
        return self.value.strftime("%d.%m.%Y")


class Record:                                   # Stores name and phone numbers
    def __init__(self, name: str):
        self.name = Name(name)                  # Name object
        self.phones: list[Phone] = []           # Phone numbers are saved as List
        self.birthday: Birthday | None = None   # Optional birthday field

    def add_phone(self, phone: str):     # Creates Phone to this record
        phone_obj = Phone(phone)         # May raise ValueError if invalid
        self.phones.append(phone_obj)

    def remove_phone(self, phone: str):  # Search by string and removes number
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)
                break                    # Stops after first match

    def edit_phone(self, old_phone: str, new_phone: str):
        # Edit existing phone: replace old with new
        for ph in self.phones:
            if ph.value == old_phone:
                ph_new = Phone(new_phone) # Validate new phone
                ph.value = ph_new.value
                return
        raise ValueError("Old phone number not found in record.")
        # Raise ValueError if not found

    def find_phone(self, phone: str):     # Search for phone number or None
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None
    
    def add_birthday(self, birthday_str: str):   # Add birthday to the contact
        self.birthday = Birthday(birthday_str)   # ValueError if format is incorrect

    def __str__(self) -> str:
        phones_str = "; ".join(p.value for p in self.phones) if self.phones else "no phones"
        birthday_str = str(self.birthday) if self.birthday else "no birthday"
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}"


class AddressBook(UserDict):                     # Class for storing and managing records

    def add_record(self, record: Record):        # Adds Record as an object to self.date by key
        self.data[record.name.value] = record    # key = record.name.value

    def find(self, name: str) -> Record | None:  # Search record by contact name
        return self.data.get(name)               # Returns either found Record or None

    def delete(self, name: str):                 # Delete record by contact name if exists
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days: int = 7) -> list[dict]: # define function
        today = date.today()                                       # today's date without time
        end_date = today + timedelta(days=days)
        result = []                                                # Create empty list of users with upcoming birthdays 

        for record in self.data.values():
            if record.birthday is None:
                continue                                           # skip if birthday not set

            bday_this_year = record.birthday.value.replace(year=today.year)
 
            if bday_this_year < today:                             # shift birthday to the next year if already happened
                bday_this_year = bday_this_year.replace(year=today.year + 1)

            if today <= bday_this_year <= end_date:                # check if bday is in 7 day interval
                congr_date = bday_this_year                        # Whom to congratulate

                if congr_date.weekday() >= 5:
                    shift = 7 - congr_date.weekday()               # Additional shift for Weekday
                    congr_date += timedelta(days=shift)

                result.append({                                    # add new object into the list
                    "name": record.name.value,
                    "congratulation_date": congr_date.strftime("%Y-%m-%d")
                })

        return result
    
if __name__ == "__main__":
    main()






