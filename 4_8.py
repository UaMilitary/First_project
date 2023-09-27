def game(terra, power):
    sum = power
    for user in terra:
        for list_1 in user:
            if list_1 > sum:
                break
            elif list_1 <= sum:
                sum += list_1
    return sum
#       print(user.get(field))

print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))



