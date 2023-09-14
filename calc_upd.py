result = None
operand = None
operator = None
wait_for_number = True

while True:
# введення цифh
    while wait_for_number == True:
        operand = input("Введіть довільне число: ")
        try:
            operand == float(operand)
        except ValueError:
            print(f"'{operand}' is not a number. Try again")
            continue
        wait_for_number = False
        break
    while wait_for_number == False:
        operator = input("Введіть оператор '*' чи '/' чи '+' чи '-': ")
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            operator = operator
        else:
            print("помилка введення")
            continue
        wait_for_number = True
        break
    while wait_for_number == True:
        operand2 = input("Введіть довільне число 2: ")
        try:
            operand2 == float(operand2)
        except ValueError:
            print(f"'{operand2}' is not a number 2. Try again")
            continue
        wait_for_number = True
        break
    if operator == "+":
        print(type(operand))
        print(operand)
        print(type(operand2))
        print(operand2)
        result += float(operand) + float(operand2)
        print(result)
    elif operator == "-":
        result -= float(operand) - float(operand2)
    elif operator == "/":
        result /= float(operand) / float(operand2)
    elif operator == "*":
        result *= float(operand) * float(operand2)
       
    
    


    


    
