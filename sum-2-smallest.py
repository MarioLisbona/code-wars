def sum_two_smallest_numbers(numbers):
    if len(numbers) >=3:
        numbers.sort()
        return numbers[0] + numbers[1]


print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))