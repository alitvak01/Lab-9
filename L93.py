#Authors are Aliza Litvak & Rylee Taylor
def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index +=1
        else:
            index +=1
    return total
