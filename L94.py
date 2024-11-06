#Authors are Aliza Litvak Rylee Taylor
def until_dot(string):
    index = 0
    s = string
    while index < len(s) and s[index] != ".":
        index += 1
    if s[index] == ".":
        print(s[:index])
