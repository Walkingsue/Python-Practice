menu = {"pan dulce": 2.00, 
"coca cola": 1.50, 
"pan": 1.00, 
"chocolate": 3.15, 
"jamon": 2.50}

cart = []
total = 0.0

print("--------MENU--------")
for item, price in menu.items():
    print(f"{item.title()}: ${price:.2f}")
print("--------------------")

while True:
    food = input("What would you like to order(q to quit)?: ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart)
for food in cart:
    total += menu.get(food)
    print(food, end=' ')

print()
print(f"Your total is: ${total:.2f}")