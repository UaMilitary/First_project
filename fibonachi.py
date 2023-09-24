def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fn = fibonacci(n-1)+fibonacci(n-2)
        return fn
 
fibonachi_row = int(input("Введіть номер числа фібоначі для вивиду ряду: "))

for i in range(0, fibonachi_row+1):
    if len(i) < 2 and len(fibonacci(i)) < 2:
        print(i, end=" ")
    elif len(i) < 2 and len(fibonacci(i)) >= 2:    
        print(i, end="  ")
    print(fibonacci(i))
for i in range(0, fibonachi_row+1):
    if len(i) < 2 and len(fibonacci(i)) < 2:
        print(i)
        print(fibonacci(i))
    print(i, end="     ")
    print(fibonacci(i))
