# перевірка довжини рядка без символів [\n, \f, \r, \t, \v]

def real_len(text):
    text = text.replace("\n", "").replace("\f", "").replace("\r", "").replace("\t", "").replace("\v", "")
    return len(text)


c = "Al\nKdfe23\t\v.\r"
print(real_len(c))