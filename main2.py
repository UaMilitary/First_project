message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
        is_upper = ch.isupper()
        ch = ch.lower()
        pos = ord(ch) - ord('a')
        new_pos = (pos + offset) % 26
        new_ch = chr(new_pos + ord('a'))
        if is_upper:
            new_ch = new_ch.upper()
        encoded_message += new_ch
    else:
        encoded_message += ch
        print(encoded_message)