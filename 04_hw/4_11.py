def is_valid_password(password):
    l = "" 
    a = False
    b = False
    c = False
    d = False
    if len(password) == 8:
        a = True
    for i in password:
        try:
            if int(i) in range(0, 9):
                b = True
        except:
            l += i
    letter = l
    for i in letter:
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            c = True
            break
    for i in letter:
        if ord(i) >= ord("A") and ord(i) <= ord("Z"):
            d = True
            break
    if a and b and c and d:
        result = True
    else:
        result = False
    return result
    
passw = "3^5a78A^"        
print(is_valid_password(passw))     