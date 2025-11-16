# Address Book CLI --- Homework 12

*A Python command‑line assistant with persistent storage (pickle)*

## 📌 Overview

This project implements an interactive **command‑line assistant** that
manages an **Address Book**.\
It supports contacts, phone numbers, birthdays --- and most importantly
for HW12 --- **persistent storage using pickle**.

When the program starts, it automatically **loads saved data**.\
When the user exits, it **saves the AddressBook to disk** so nothing is
lost between sessions.

------------------------------------------------------------------------

## 🚀 Features

### ✅ Address Book Functionality

-   Add contacts\
-   Add multiple phone numbers\
-   Edit phone numbers\
-   Delete phone numbers\
-   Add a birthday\
-   Show a birthday\
-   List birthdays in upcoming 7 days\
-   Show all contacts\
-   View phone numbers for a contact

### 🔒 Persistence (HW12)

Implemented via **pickle**: - `save_data(book)` --- saves the full
AddressBook to `addressbook.pkl` - `load_data()` --- loads it back when
the app starts - Data persists across program runs

### 🧠 OOP Architecture

-   `Field` --- base class\
-   `Name`, `Phone`, `Birthday` --- field classes\
-   `Record` --- represents a single contact\
-   `AddressBook` --- extended dictionary storing Records

### 🛠 Copying Logic (Lesson 12)

-   Custom `__copy__` (shallow copy)
-   Custom `__deepcopy__` (deep copy)
-   Custom serialization via `__getstate__` / `__setstate__`

------------------------------------------------------------------------

## 📝 Available Commands

  Command                              Description
  ------------------------------------ --------------------------------
  `add [name] [phone]`                 Add a new contact or new phone
  `change [name] [old] [new]`          Replace phone
  `phone [name]`                       Show all phones for contact
  `all`                                Show all contacts
  `add-birthday [name] [DD.MM.YYYY]`   Add birthday
  `show-birthday [name]`               Show birthday
  `birthdays`                          List birthdays in next 7 days
  `hello`                              Greet message
  `close` / `exit`                     Save and exit

------------------------------------------------------------------------

## 💾 How Persistence Works

``` python
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
```

On exit:

``` python
save_data(book)
```

------------------------------------------------------------------------

## ▶️ How to Run

    python your_script_name.py

You will see:

    Welcome to the assistant bot!
    Enter a command:

Start typing commands.

------------------------------------------------------------------------

## 📂 Project Structure

    addressbook/
    │
    ├── main.py
    ├── addressbook.pkl   # auto‑created after first run
    └── README.md

------------------------------------------------------------------------

## 📘 Example Session

    > add John 1234567890
    Contact added.

    > add John 5555555555
    Contact updated.

    > phone John
    1234567890; 5555555555

    > add-birthday John 12.03.1990
    Birthday added.

    > all
    Contact name: John, phones: 1234567890; 5555555555, birthday: 12.03.1990

    > exit
    Good bye Sweetheart!

------------------------------------------------------------------------

## ✔️ Summary

This project demonstrates: - Clean OOP design\
- Real serialization with pickle\
- State persistence\
- Custom shallow & deep copy methods\
- Custom pickling control

Perfect foundation for the next steps in building a fully functional
personal assistant.

------------------------------------------------------------------------

## Created by:
**Author:** Oleksandr Skriabikov  
Created as part of the **Neoversity Python course, Lesson 12**