def solution(string, ending):

    if len(ending) > 0:
        return string[(len(ending) * -1):] == ending
    else:
        return True

print(solution('abc', 'bc'))
print(solution('abc', 'd'))
print(solution('abc', ''))