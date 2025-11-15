from collections import UserDict

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
        super().__init__(value)

    @staticmethod
    def _is_valid(value: str) -> bool:   # Exactly 10 digits
        return value.isdigit() and len(value) == 10


class Record:                            # Stores name and phone numbers
    def __init__(self, name: str):
        self.name = Name(name)           # Name object
        self.phones: list[Phone] = []    # Phone numbers are saved as List

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

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):                     # Class for storing and managing records

    def add_record(self, record: Record):        # Adds Record as an object to self.date by key
        self.data[record.name.value] = record    # key = record.name.value

    def find(self, name: str) -> Record | None:  # Search record by contact name
        return self.data.get(name)               # Returns either found Record or None

    def delete(self, name: str):                 # Delete record by contact name if exists
        if name in self.data:
            del self.data[name]


# TEST:

if __name__ == "__main__":
    book = AddressBook()           # Create new address book

    john_record = Record("John")   # Create new contact John
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)   # Adds John to Address book

    jane_record = Record("Jane")   # Create new contact Jane
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():        # Shows all contacts in Address book
        print(record)

    john = book.find("John")        # Search and edit phone number
    john.edit_phone("1234567890", "1112223333")
    print(john)

    found_phone = john.find_phone("5555555555")   # Search for phone number in Contact
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")              # Delete contact Jane