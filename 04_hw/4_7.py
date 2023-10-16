points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
def calculate_distance(coordinates):
    n = len(coordinates)
    koord = list()
    i = 0
    dist = 0
    while i < (n-1):
        a1 = ()
        a = coordinates[i]
        b = coordinates[i+1]
        if a < b:
            a1 = (a, b)
        elif a > b:
            a1 = (b, a)
        print(a1)
        if a1 in points:
            dist += points[a1]
        i += 1
    return dist

a = [1, 3, 1, 3, 0, 1]
print(calculate_distance(a))