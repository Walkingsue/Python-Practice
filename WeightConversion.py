weight = float(input("Enter a weight in pounds: "))
unit = input("Enter the unit you want to convert to (kg or pounds): ")
if unit == "kg":
    weight = weight * 2.205
elif unit == "pounds":
    weight = weight / 2.205
else:
    print(f"{unit} is not a valid unit")
print(f"The weight in {unit} is: {round(weight), 1}")
    