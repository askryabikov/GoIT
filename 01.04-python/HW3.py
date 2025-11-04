import re 

def normalize_phone(phone_number):
    check = re.sub(r"[^\d+]", "", phone_number) # use ReGex to remove everything except + and digits
    if check.startswith("+38"): # check for international code
        return check
    elif check.startswith("380"): # add + for international number is already international
        check = "+" + check
        return check
    else:
        return "+38" + check # add ukrainian code if needed

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
] 

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Normalized ukrainian phones:", sanitized_numbers)
