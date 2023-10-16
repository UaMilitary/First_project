def prepare_data(data):
    data.sort()
    data.pop(0)
    data.pop(-1)
    return data

a = [3, 230, 1, 12, 1]
print(prepare_data(a))

