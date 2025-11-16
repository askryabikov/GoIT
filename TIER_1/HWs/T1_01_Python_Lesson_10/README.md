# Personal Assistant — CLI Contact Book

This project is a console-based assistant bot that manages contacts, phone numbers, birthdays, and more.  
It is built as part of an educational assignment following OOP principles in Python.

## Features (Commands Overview)

```
add [name] [phone]             → Add a new contact or append a phone
change [name] [old] [new]      → Change an existing phone number
phone [name]                   → Show all phone numbers for a contact
all                            → Show all contacts
add-birthday [name] [DD.MM.YYYY] → Add birthday to a contact
show-birthday [name]           → Show contact's birthday
birthdays                      → Show upcoming birthdays within 7 days
hello                          → Greeting from the bot
close / exit                   → Exit program
```

## Project Structure

```
main.py       → Main CLI logic + command handlers
AddressBook   → Stores all records, supports search/delete/iteration
Record        → Represents a single contact (name, phones, birthday)
Field         → Base field class
Phone         → Validates a 10-digit phone number
Birthday      → Validates date format DD.MM.YYYY
```

## How It Works

- All contact data is stored inside an AddressBook (inherits from UserDict)
- Each contact is a Record containing:
  - Name
  - list of Phone objects
  - optional Birthday
- Data validation:
  - Phone numbers must be 10 digits
  - Birthday must follow DD.MM.YYYY
- Bot handles user errors using a decorator @input_error
- Birthdays are calculated using datetime and adjusted for weekends

## Running the Bot

Make sure you have Python 3.10+

Run:

```
python main.py
```

Then type commands as shown in the list above.

## Validation Rules

| Field | Rule |
|-------|------|
| Phone | Must be exactly 10 digits |
| Birthday | Format must be DD.MM.YYYY |
| Commands | Any input errors handled by @input_error |

## Technologies Used

- Python 3 (OOP)
- datetime module
- Decorators
- Custom dunder methods (__str__, __repr__, __contains__, __iter__)
- Functional programming elements

## Created by:
**Author:** Oleksandr Skriabikov  
Created as part of the **Neoversity Python course, Lesson 10**
