def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fn = fibonacci(n-1)+fibonacci(n-2)
        return fn


fibonachi_row = int(input("Введіть номер числа фібоначі для вивиду ряду: ")) 
print(f"{fibonacci(fibonachi_row)}")
