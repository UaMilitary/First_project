import sys


def parse_args():
    result = ""
    a = (len(sys.argv))
    if a == 1:
        result = ""
    elif a == 2:
        result = f"{sys.argv[1]}"
    elif a >= 3:
        for arg in sys.argv:
            result += f"{arg} "
           
    return result

print(parse_args())

