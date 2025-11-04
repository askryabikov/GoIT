from datetime import datetime, timedelta # enable date objects from datetime module

def get_upcoming_birthdays(users): # define function
    today = datetime.today().date() # today's date without time
    result = [] # Create empty list of users with upcoming birthdays 

    for user in users:  # enables cycle for checking each user
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # get string with date, transform into date object and leave date only

        birthday_this_year = birthday.replace(year=today.year) 
        if birthday_this_year < today: # shift birthday to the next year if already happened
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_diff = (birthday_this_year - today).days # only for today and next 7 upcoming days
        if 0 <= days_diff <= 7:
            celebration_date = birthday_this_year
            if celebration_date.weekday() == 5:      # Additional shift for Saturday
                celebration_date += timedelta(days=2)
            elif celebration_date.weekday() == 6:    # Additional shift for Sunday
                celebration_date += timedelta(days=1)

            result.append({  # add new object into the list
                "name": user["name"],
                "congratulation_date": celebration_date.strftime("%Y.%m.%d")
            })

    return result

users = [  # List
    {"name": "John Doe", "birthday": "1985.11.07"},
    {"name": "Jane Smith", "birthday": "1990.11.08"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of upcoming birthdays for this week: ", upcoming_birthdays)