message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ord(ch) >= ord("a") and ord(ch) <= ord("z") and offset != 0:
        if (ord(ch) + offset % 26) > ord("z"):
            new_ch = (ord("a") + offset % 26 - 1) - (ord("z")- ord(ch))
            encoded_message += chr(new_ch)
        elif (ord(ch) + offset % 26) <= ord("z"):
            new_ch = (ord(ch) + offset % 26)
            encoded_message += chr(new_ch)
    elif ord(ch) >= ord("A") and ord(ch) <= ord("Z") and offset != 0:
        if (ord(ch) + offset % 26) > ord("Z"):
            new_ch = (ord("A") + offset % 26 - 1) - (ord("Z")- ord(ch))
            encoded_message += chr(new_ch) 
        elif (ord(ch) + offset % 26) <= ord("Z"):
            new_ch = (ord(ch) + offset % 26)
            encoded_message += chr(new_ch)
    else:
        new_ch = ch
        encoded_message += ch
print(encoded_message)


