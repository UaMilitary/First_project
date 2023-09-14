result = None
operand = None
operator = None
wait_for_number = True

while True:
# введення цифh
    while True:
        operand = input("Введіть довільне число: ")
        try:
            operand == float(operand)
        except ValueError:
            print(f"'{operand}' is not a number. Try again")
            continue
        break
    print(operand)
# перевірка
    while True:
        operator = input("Введіть оператор '*' чи '/' чи '+' чи '-': ")
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "/":
                result /= operand
            elif operator == "*":
                result *= operand
            print (operator)
        else:
            print("помилка введення")
            continue
        break


    


    
