def split_list(grade):
    n = len(grade)
    a = list()
    b = list()
    if n > 1:
        aver = sum(grade)/len(grade)
        for i in grade:
            if i <= aver:
                a.append(i)
            else:
                b.append(i)
    elif n == 1:
        a = list(grade)
    tuple3 = (a, b)
    return tuple3

d = [1, 2]
print(split_list(d))

