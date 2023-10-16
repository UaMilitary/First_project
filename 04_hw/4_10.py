from random import randint
def get_random_password():
    c = ""
    while True:
        b = randint(40, 126)
        c += chr(b)
        if len(c) >= 8:
            break
    return c

print(get_random_password())

    
    
        
        
        
