# AddressBook — Object-Oriented Contacts Manager

This project implements an **Address Book** using **Object-Oriented Programming** in Python.  
It continues the development of a virtual assistant from the previous homework, but here the focus is fully on **data models**, not CLI interaction.

---

## 📌 Project Description

The system is built using several classes that work together:

### **Field**
Base class for all data fields. Stores a value and provides a string representation.

### **Name**
Represents the name of a contact.  
Mandatory field. Inherits from `Field`.

### **Phone**
Represents a phone number.  
Includes **validation** — the number must contain **exactly 10 digits**, otherwise a `ValueError` is raised.

### **Record**
Represents a single contact.  
Stores:
- the contact's **name**
- a list of **phone numbers**

Provides functionality:
- `add_phone()`
- `remove_phone()`
- `edit_phone()`
- `find_phone()`

### **AddressBook**
The collection of all contact records.  
Inherits from Python’s `UserDict`.

Supports:
- `add_record()`
- `find()`
- `delete()`

---

## 📂 Example Usage

```python
book = AddressBook()

# Create record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

# Create record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Print all contacts
for name, record in book.data.items():
    print(record)

# Edit John's phone
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

# Find one of John's numbers
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Delete Jane
book.delete("Jane")
```

---

## 🧪 Output Example

```
Contact name: John, phones: 1234567890; 5555555555
Contact name: Jane, phones: 9876543210
Contact name: John, phones: 1112223333; 5555555555
Name: John: 5555555555
```

---

## ✔️ Requirements for Assignment

This solution fully implements:

- Field, Name, Phone classes  
- Phone validation  
- Record with multiple phones  
- AddressBook with add/find/delete operations  
- Objects interacting exactly as described in the task  

---

## 👤 Author
**Alexander Skriabikov**  
Python Student — GoIT Academy  
Moldova, Chisinau
