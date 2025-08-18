foods = []
prices = []
total = 0

while True:
    food = input("Enter the food (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price for {food}: "))
        foods.append(food)
        prices.append(price)
        
for food in foods:
    print(food, end=' ')

for price in prices:
    total += price

print(f"\nTotal price: {total:.2f}")
