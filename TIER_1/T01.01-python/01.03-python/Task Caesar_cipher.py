message = "Brute is a killer"

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = "NDGFQ UE BXMZZUZS FA WUXX YQ"
cipher = ""
key = -1234

for letter in text.upper():
    if letter in alpha:
        letter_index = (alpha.find(letter) + key) % len(alpha)  # 5 -> 8
        cipher += alpha[letter_index]
    else:
        cipher += letter

print(cipher)




# ИЛИ

def crypt_message(message, key):
    message = message.upper()
    key = 3
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in text.upper():
        if letter in alpha: # if the letter is a ctually a letter
            letter_index = (alpha.find(letter) + key) % len(alpha)  # 5 -> 8
            cipher += alpha[letter_index]
        else:
            cipher += letter
            
    return result

cipher = crypt_message("Brute is a killer", 3)
print(cipher)


