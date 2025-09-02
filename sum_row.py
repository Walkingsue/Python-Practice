def row_sum_odd_numbers(*n):
    if type(n) == int and n > 0:
        return n**3
    else:
        print('it is not a valid value')

print(row_sum_odd_numbers(1))