

from datetime import datetime # imported module datetime

def get_days_from_today(date: str) -> int: # defined function
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date() # string parse time
        today = datetime.today().date() # Date today
        date_delta = today - input_date # Calculate date difference in days
        return date_delta.days # Return difference in days
    except ValueError:
        print("Incorrect input. Use YYYY-MM-DD date format, please.")
    

print(get_days_from_today("2021-10-09")) # Date in the past
print(get_days_from_today("2028-11-04")) # Date in the future
print(get_days_from_today("2025-13-11")) # Incorrect input check with Value Error
