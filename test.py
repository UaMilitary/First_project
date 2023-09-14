def cost_delivery(quantity, *products, discount=0):
    count = 0
    summ = 0
    for i in range (1, quantity+1):
        if i == 1:
            cost = 5
        else:
            cost = (i-count) * 2
        summ += cost
        count += 1
    total = summ * (1 - discount)
    return total

print(cost_delivery(2, 1, 2, 3))