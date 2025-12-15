from collections import deque 

def is_palindrome(text):  
    clean_text = ""              # empty string
    for ch in text:              # check each letter
        if not ch.isspace():     # ignore spaces
            clean_text += ch.lower()   # make lowercase and add to clean_text

    d = deque(clean_text)        # put all characters into deque

    while len(d) > 1:            # if there are at least 2 characters
        left_char = d.popleft()  # take from the left side
        right_char = d.pop()     # take from the right side
        if left_char != right_char:    # and compare both ends
            return False         # if not a palindrome

    return True                  # if all pairs coincide

text = input("Enter text: ")     # input from user

if is_palindrome(text):       
    print("Palindrome")          
else:
    print("Not palindrome")
