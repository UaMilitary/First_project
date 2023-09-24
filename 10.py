num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    for i in range(0, (num + 1)):
        sum = sum + i
    print(sum, end= " ")
    num = int(input("Enter integer (0 for output): "))