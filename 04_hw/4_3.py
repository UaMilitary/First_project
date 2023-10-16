def format_ingredients(items):
    items.insert(-1, "and")
    add = ""
    if len(items) >= 3:
        for i in items:
            if i != items[-1] and i != items[-2] and i != items[-3]: 
                add += f"{i}, "
            elif i == items[-2] or i == items[-3]:
                add += f"{i} "
            else:
                add += f"{i}"   
    if len(items) == 2:
            a = items[1]
            add = a
    return add

print(format_ingredients(["a"]))