"""        |  |  |  |  |  |
           |  |  |  |  |  |
           |  |  |  |  |  |
           |  |  |  |  |  |
           |  |  |  |  |  | """

world_map = ""
size_c = 5
size_r = 5
i = 0
j = 0
world_map = ""
char_x = 0
char_y = 0
for i in range(size_r):
    print("i")
    row = "|"
    for j in range(size_c):
        row += "  |"
        print("j")
    world_map += f"{row}\n"
print(world_map)