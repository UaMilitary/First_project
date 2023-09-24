sum = 0
num = int(input("Enter integer (0 for output): "))
while num != 0:
    total = num / 2 * (num + 1)
    sum = sum + total
    print(sum)
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        print(f"обрахунок закінчено, загальна сумма {sum}")
        break

