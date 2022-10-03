def order(sentence):
    x = sentence.split(' ')

    sort_dict = {}

    for i in x:
        for y in i:
            if y.isnumeric():
                sort_dict[y] = i


    result = dict(sorted(sort_dict.items()))


    return ' '.join(result[item] for item in result)

print(order('is2 Thi1s T4est 3a'))
print(order('4of Fo1r pe6ople g3ood th5e the2'))