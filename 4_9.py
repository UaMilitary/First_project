def is_valid_pin_codes(pin_codes):
    a = True
    b = True
    c = True
    d = True 
    if len(set(pin_codes)) != len(pin_codes) or len(pin_codes) < 1:
        a = False
    for val in pin_codes:
        try:
            if len(val) != 4:
                b = False
                break
        except TypeError:
            b = False
            break
        if type(val) != str:
            c = False
            break
        for n in val:
            try:
                int(val)
            except ValueError:
                d = False
        if d == False:
            break   
    if a and b and c and d:
        result = True
    else:
        result = False
    return result




a = []
print(is_valid_pin_codes(a))
