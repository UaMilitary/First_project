from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num


def get_password():
    count = 0
    while True:
       find_psw = get_random_password()
       if is_valid_password(find_psw) == True:
           psw = find_psw
           break
       else:
           count += 1
           if count >= 100:
               break
           continue
    return psw

print(get_password())
