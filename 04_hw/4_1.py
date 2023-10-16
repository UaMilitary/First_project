def amount_payment(payment):
    sum = 0
    for i in payment:
        if i > 0:
           sum += i
    return sum

a = [1, 4, -5]
print(amount_payment(a))

b = [1, 4, -5]
print(amount_payment(b))