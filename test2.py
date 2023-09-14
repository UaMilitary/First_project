"""        |  |  |  |  |  |
           |  |  |  |  |  |
           |  |  |  |  |  |
           |  |  |  |  |  |
           |  |  |  |  |  | """

world_map = ""
size_r = 3
size_c = 3
count_level = 1
while True:
    print(f"Level {count_level}")
    count_step = 0
    char_x = 0
    char_y = 0
    exit_x = size_c-1
    exit_y = size_r-1
    while True:
        i = 0
        j = 0
        world_map = ""
        while j < size_r:
            i = 0
            row = "|"
            while i < size_c:
                if char_x == i and char_y == j:
                    if char_x == exit_x and char_y == exit_y:
                       row += "W|"
                    else:    
                       row += "X|"
                elif exit_x == i and exit_y == j:
                    row += "O|"
                else:
                    row += " |"   
                i +=1
            j +=1
            world_map += f"{row}\n"
        print(world_map)
        if char_x == exit_x and char_y == exit_y:
            print("You are Winner!!!")
            size_r += 1
            size_c += 1
            break
        direction = input("Enter direction (r/l/d/u): ")    
        if direction == "u" and char_y > 0:
            char_y -= 1
        elif direction == "d" and char_y < (size_r-1):
            char_y += 1
        elif direction == "r" and char_x < (size_c-1):
            char_x += 1
        elif direction == "l" and char_x > 0:
            char_x -= 1
        count_step += 1
        print(f"count_step {count_step}")
    count_level += 1


        

    
        

