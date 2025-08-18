vegies = ["carrot", "broccoli", "spinach"]
fruit = ["apple", "banana", "cherry"]
meat = ["chicken", "beef", "pork"]

grocery_list = [vegies, fruit, meat]
for element in grocery_list:
    for item in element:
        print(item, end=' ')
    print()  # New line after each category