import math

def get_middle(s):
    if len(s) % 2 == 0:
        return s[((len(s) // 2) - 1):((len(s) // 2) + 1)]
    else:
        return s[(math.ceil(len(s) / 2) - 1)]


print(get_middle('test'))
print(get_middle('testing'))
print(get_middle('middle'))
