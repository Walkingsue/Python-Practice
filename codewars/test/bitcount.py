def count_bit(number):
    sum = 0
    num_in_bit = bin(number)[2:]
    for num in num_in_bit:
        sum += int(num)
    return sum

