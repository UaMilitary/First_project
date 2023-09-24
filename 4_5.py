def lookup_key(data, value):
    a = list()
    for key, val in data.items():
        if val == value:
            a.append(key)
    return a
            
print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))

#lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2)==['key2', 'key4']
