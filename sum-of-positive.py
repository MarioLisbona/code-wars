def positive_sum(arr):
    if len(arr) == 0:
        return 0
    result = 0

    for i in arr:
        if i > 0:
            result += i
    
    return result

print(positive_sum([1,-4,7,12]))