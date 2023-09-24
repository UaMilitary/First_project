result = 0
operand = None
operator = None
wait_for_number = True
while True:
    
    # введення математичних операторів
    while wait_for_number == False:
        operator = input("Введіть математичний оператор '*' чи '/' чи '+' чи '-' чи '=': ")
        if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "=":
            operator = operator
        else:
            print("помилка введення")
            continue
        wait_for_number = True
        print(operator)
        break

    # введення чисел
    while wait_for_number == True and operator != "=":
        operand = input("Введіть довільне число: ")
        try:
            operand == float(operand)
        except ValueError:
            print(f"'{operand}' is not a number. Tr1+y again")
            continue
        wait_for_number = False
        break
    
    # розрахунок 
    if operator == None:
        result = float(operand)
        print(result)
    elif operator == "+":
        result += float(operand)
    elif operator == "-":
        result -= float(operand)
    elif operator == "/":
        try:
            result /= float(operand)
        except ZeroDivisionError:
            print(f"ділення на 0, введіть інше число та повторіть оерацію")
            result = 0
            operator = None
            operand = None
            wait_for_number = True
    elif operator == "*":
        result *= float(operand)
    elif operator == "=":
        result = result
        print(f"Результат дорівнює {result}")
        break