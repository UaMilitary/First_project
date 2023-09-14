message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ord(ch) >= ord("a") and ord(ch) <= ord("z"):
        pos = ord('ch') - ord('a')
        pos = (pos + offset) % 26
        encoded_message = chr(pos + ord("a"))
    elif ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
        pos = ord('ch') - ord('A')
        pos = (pos + offset) % 26
        encoded_message = chr(pos + ord("A"))
    else:
        encoded_message = encoded_message + ch
    encoded_message = encoded_message + 1

