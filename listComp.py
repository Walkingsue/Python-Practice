numb = [1, 2 , 4, 8, 16, 25, 63, -73, -15]

even_numb = [num for num in numb if num % 2 == 0]
odd_numb = [num for num in numb if num % 2 == 1]

positive_numb = [num for num in numb if num >= 0]
negative_numb = [num for num in numb if num < 0]

print(even_numb)
print(odd_numb)
print(positive_numb)
print(negative_numb)
