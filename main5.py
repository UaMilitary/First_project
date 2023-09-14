try:
    num = int(input("Введіть розмір команди: "))
except ValueError:
    print("Ви ввели не число!")
except ZeroDivisionError:
    print("Ви ввели нуль учасників!")
else:
    award = 10000
    bonus_for_person = award / num
    print(f"Нагорода кожному учаснику {bonus_for_person} золота!")
finally:
    print("До побачення!")