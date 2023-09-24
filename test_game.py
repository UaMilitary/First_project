from random import randint, choice

SIZE_R = randint(4, 7)
SIZE_C = randint(4, 7)

def game_conditions(char_x, char_y, enemy_x, enemy_y,
                    exit_x, exit_y, char_sign):
    win_condition = char_x == exit_x and char_y == exit_y
    loss_condition = char_x == enemy_x and char_y == enemy_y
    if win_condition:
        char_sign = "W|"
        print("You are winner!!!")
    elif loss_condition:
        char_sign = "L|"
        print("You are loser!!!")
    return char_sign, win_condition or loss_condition



def map_built(char_x, char_y, enemy_x, enemy_y,
             exit_x, exit_y, char_sign,
             size_r=SIZE_R, size_c=SIZE_C):
    world_map = ""
    for j in range(size_r):
        row = "|"
        for i in range(size_c):
            if char_x == i and char_y == j:
                row += f"{char_sign}"
            elif exit_x == i and exit_y == j:
                row += "O|"
            elif enemy_x == i and enemy_y == j:
                row += "E|"
            else:
                row += " |"   
        world_map += f"{row}\n"
    return world_map

def move(direction, x, y, size_r=SIZE_R, size_c=SIZE_C):
    if direction == "u" and y > 0:
        y -= 1
    elif direction == "d" and y < (size_r-1):
        y += 1
    elif direction == "r" and x < (size_c-1):
        x += 1
    elif direction == "l" and x > 0:
        x -= 1
    return x, y

char_sign = "X|"

char_x = randint(0, SIZE_C - 1)
char_y = randint(0, SIZE_R - 1)

world_map = ""


enemy_x = randint(0, SIZE_C - 1)
enemy_y = randint(0, SIZE_R - 1)

exit_x = randint(0, SIZE_C - 1)
exit_y = randint(0, SIZE_R - 1)


while True:

    char_sign, cond_flag = game_conditions(char_x, char_y, enemy_x, enemy_y,
                                           exit_x, exit_y, char_sign)
        
    world_map = map_built(char_x, char_y, enemy_x, enemy_y,
            exit_x, exit_y, char_sign,
            size_r=SIZE_R, size_c=SIZE_C)
    print(world_map)

    if cond_flag:
        break
    
    direction = input("Enter direction (r/l/d/u): ")    
    char_x, char_y = move(direction, char_x, char_y)

    enemy_direction = choice("udlr")    
    enemy_x, enemy_y = move(enemy_direction, enemy_x, enemy_y)

    

    




        

    
        

