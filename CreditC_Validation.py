card_numb = input("Enter your credit card number: ")

total = 0
sum_even_numb = 0
sum_odd_numb = 0

card_numb = card_numb.replace("-", "")
card_numb = card_numb.replace(" ", "")

for num in card_numb[::2]: 
    sum_odd_numb += int(num)

for num in card_numb[1::2]: 
    x = int(num) * 2
    if x >= 10:
        sum_even_numb += (1 +(x % 10))
    else:
        sum_even_numb += x

total = sum_even_numb + sum_odd_numb

if total % 10 == 0:
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")