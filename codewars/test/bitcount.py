def count_bit(number):
    sum = 0
    num_in_bit = bin(number)[2:]
    for num in num_in_bit:
        sum += int(num)
    return sum

#Otra forma de escribir esto seria 

def new_count_bits(number):
    return bin(number).count("1")

print(new_count_bits(1234))