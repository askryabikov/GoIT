# HW 12 - Oleksandr Skriabikov
# Commands:
#   add [name] [phone]
#   change [name] [old_phone] [new_phone]
#   phone [name]
#   all
#   add-birthday [name] [DD.MM.YYYY]
#   show-birthday [name]
#   birthdays
#   hello
#   close / exit

import pickle                                    # New 
import copy                                      # New
from collections import UserDict
from datetime import datetime, date, timedelta   # for birthdays

# PART I - FUNCTIONS

def input_error(func):            # decorator to handle user input errors
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:   # e may have its own message
            return str(e) or "Give me name and phone please."
        except KeyError:          # in case contact not found in dictionary
            return "Contact not found."
        except IndexError:        # in case no name provided 
            return "Enter the argument for the command."
    return inner


def parse_input(user_input: str):
    cmd, *args = user_input.split()   # split by spaces into command and arguments
    cmd = cmd.strip().lower()         # remove upper case and spaces
    return cmd, *args


@input_error
def add_contact(args, book) -> str:
    """Add new contact or new phone to existing contact in AddressBook"""
    if len(args) < 2:
        # will be caught by decorator as ValueError
        raise ValueError

    name = args[0]    # name as 1st argument
    phone = args[1]   # phone as 2nd argument

    record = book.find(name)      # find existing record or create new one
    if record is None:
        record = Record(name)     # create new contact
        book.add_record(record)   # save to AddressBook
        message = "Contact added."
    else:
        message = "Contact updated."

    record.add_phone(phone)       # add phone to this contact
    return message


@input_error
def change_contact(args, book) -> str:
    """
    Change existing phone to new phone for given contact.

    Outcome:
        change [name] [old_phone] [new_phone]
    """
    if len(args) < 3:        # need name + old_phone + new_phone
        raise ValueError("Give me name, old phone and new phone please.")

    name = args[0]           # 1st argument = contact name
    old_phone = args[1]      # 2nd argument = old phone to replace
    new_phone = args[2]      # 3rd argument = new phone

    record = book.find(name)
    if record is None:       # decorator will write "Contact not found"
        raise KeyError

    # record.edit_phone will raise ValueError if old number not found
    record.edit_phone(old_phone, new_phone)

    return "Contact updated."


@input_error
def show_phone(args, book) -> str: 
    """Shows all phone numbers for given contact name"""
    if len(args) < 1:               # Counts arguments
        raise IndexError            # Error if no arguments

    name = args[0]                  # Name as 1st argument
    record = book.find(name)        # Searches for the contact
    if record is None:              # Error if not found
        raise KeyError

    if not record.phones:
        return "No phones for this contact."

    return "; ".join(phone.value for phone in record.phones) # Join numbers with " ; "


@input_error
def show_all(book) -> str:   
    """Shows all contacts in AddressBook"""
    if not book.data:      # In case Address book is empty
        return "No contacts saved."

    lines = []                           # Prepares a list for each contact
    for record in book.data.values():    # cycle to search through all records
        # use __str__ from Record (name, phones, birthday)
        lines.append(str(record))        # converts each record into string
    return "\n".join(lines)              # each contact will be on a new line


@input_error
def add_birthday(args, book) -> str:
    """
    Add birthday to existing contact.

    Outcome:
        add-birthday [name] [DD.MM.YYYY]
    """
    if len(args) < 2:
        raise ValueError("Give me name and birthday in format DD.MM.YYYY.")

    name = args[0]
    birthday_str = args[1]

    record = book.find(name)
    if record is None:
        raise KeyError    # "Contact not found."

    record.add_birthday(birthday_str) # checks date format + can raise ValueError
    return "Birthday added."


@input_error
def show_birthday(args, book) -> str:
    """
    Shows birthday for given contact

    Outcome:
        show-birthday [name]
    """
    if len(args) < 1:
        raise IndexError   # "Enter the argument for the command."

    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError

    if record.birthday is None:
        return "Birthday is not set for this contact."

    return f"{name}'s birthday is {record.birthday}"


@input_error
def birthdays(args, book) -> str:
    """
    Shows list of contacts to congratulate in next 7 days.

    Command:
        birthdays
    (igonres args but keeps them for decorator compatibility)
    """
    upcoming = book.get_upcoming_birthdays(days=7)
    if not upcoming:
        return "No birthdays in the next 7 days."

    lines = []
    for item in upcoming:   # item = {"name": ..., "congratulation_date": "YYYY-MM-DD"}
        name = item["name"]
        date_str = item["congratulation_date"]
        lines.append(f"{name}: {date_str}")

    return "Upcoming birthdays:\n" + "\n".join(lines)


def save_data(book: "AddressBook", filename: str = "addressbook.pkl"):   # - New
    """Save AddressBook into file using pickle"""
    with open(filename, "wb") as f:        # wb stands for write binary
        pickle.dump(book, f)               # f - creating file object


def load_data(filename: str = "addressbook.pkl") -> "AddressBook":       # - New
    """Load AddressBook from file (if exists) or create new one"""
    try:
        with open(filename, "rb") as f:    # rb - read binary
            book = pickle.load(f)
            if not isinstance(book, AddressBook):   # checks file
                return AddressBook()                # Starts with empty book if file is corrupted
            return book
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()                      # New - AddressBook changed to loading file
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)   # unpack command and arguments

        if command in ["close", "exit"]:
            save_data(book)                        # New - Saves data
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

        elif command == "add-birthday":
            result = add_birthday(args, book)
            print(result)

        elif command == "show-birthday":
            result = show_birthday(args, book)
            print(result)

        elif command == "birthdays":
            result = birthdays(args, book)
            print(result)

        else:
            print("Invalid command.")



# PART II - CLASSES

class Field:              # Base class for all record fields
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:    # for users
        return str(self.value)

    def __repr__(self) -> str:   # for developers
        return f"{self.__class__.__name__}({self.value!r})"
        # self.__class__.__name__   - gets the name of the class
        # self.value!r              - !r for repr instead of strings


class Name(Field):        # Mandatory field
    pass


class Phone(Field):       # Phone field with 10 digits validation
    def __init__(self, value: str):
        if not self._is_valid(value):    # In case of incorrect input
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)         

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
        # Raise ValueError if not found (will be shown to user by decorator)
        raise ValueError("Old phone number not found in record.")

    def find_phone(self, phone: str):     # Search for phone number or None
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None
    
    def add_birthday(self, birthday_str: str):   # Add birthday to the contact
        self.birthday = Birthday(birthday_str)   # ValueError if format is incorrect

    def __str__(self) -> str:                    # format as __str__
        phones_str = "; ".join(p.value for p in self.phones) if self.phones else "no phones"
        birthday_str = str(self.birthday) if self.birthday else "no birthday"
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}"

    def __repr__(self) -> str:   # debug / console-friendly representation
        return f"Record(name={self.name!r}, phones={self.phones!r}, birthday={self.birthday!r})"
    

    def __copy__(self):                                  # New - Lesson 12 - Shallow copy
        new_record = Record(self.name.value)             # settings for shallow copy
        new_record.phones = self.phones                  # creates record and path to objects
        new_record.birthday = self.birthday
        return new_record

    def __deepcopy__(self, memo=None):                   # New - Lesson 12 - Deep copy
        if memo is None:                                 # creates copy of all objects inside
            memo = {}                                    # settings for deep copy:
        new_record = Record(copy.deepcopy(self.name.value, memo))   # memo does not allow double copying
        new_record.phones = copy.deepcopy(self.phones, memo)
        new_record.birthday = copy.deepcopy(self.birthday, memo)
        return new_record


class AddressBook(UserDict):                     # Class for storing and managing records

    def add_record(self, record: Record):        # Adds Record as an object to self.data by key
        self.data[record.name.value] = record    # key = record.name.value

    def find(self, name: str) -> Record | None:  # Search record by contact name
        return self.data.get(name)               # Returns either found Record or None

    def delete(self, name: str):                 # Delete record by contact name if exists
        if name in self.data:
            del self.data[name]

    def __contains__(self, name: str) -> bool:   # provides using "in" in AddressBook
        return name in self.data                 # self.data = dict, where keys = names

    def __iter__(self):                          # iterates through AddressBook
        return iter(self.data.values())

    def __repr__(self) -> str:                   # Shows summary
        return f"AddressBook(records={list(self.data.keys())})"
    
    def __getstate__(self):                      # New
        return self.data                         # what to save/ignore in pickle

    def __setstate__(self, state):               # New
        self.data = state                        # how to restore data

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
                    shift = 7 - congr_date.weekday()               # Additional shift for weekend
                    congr_date += timedelta(days=shift)

                result.append({                                    # add new object into the list
                    "name": record.name.value,
                    "congratulation_date": congr_date.strftime("%Y-%m-%d")
                })

        return result
    

if __name__ == "__main__":
    main()
