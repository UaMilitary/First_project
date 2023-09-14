result = 0
operand = None
operator = None
wait_for_number = True
while True and operator != "=":
# введення цифр
    while wait_for_number == False and operator != "=":
        operator = input("Введіть оператор '*' чи '/' чи '+' чи '-' чи '='")
        if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "=":
            operator = operator
        else:
            print("помилка введення")
            continue
        wait_for_number = True
        print(operator)
        break
    while wait_for_number == True and operator != "=":
        operand = input("Введіть довільне число: ")
        try:
            operand == float(operand)
        except ValueError:
            print(f"'{operand}' is not a number. Try again")
            continue
        wait_for_number = False
        print(operand)
        print(operator)
        break
    
    if operator == None:
        result = float(operand)
        print(f"результат дорівнює {result}")
    elif operator == "+":
        result += float(operand)
        print(f"результат дорівнює {result}")
    elif operator == "-":
        result -= float(operand)
        print(f"результат дорівнює {result}")
    elif operator == "/":
        try:
            result /= float(operand)
        except ZeroDivisionError:
            print(f"ділення на 0, введіть інше число та повторіть оерацію")
            result = 0
            operator = None
            operand = None
            wait_for_number = True
        print(f"результат дорівнює {result}")
    elif operator == "*":
        result *= float(operand)
        print(f"результат дорівнює {result}")
    while operator == "=":
        result = result
        print(f"фінальний результат дорівнює {result}")
        break