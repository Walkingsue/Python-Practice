val1 = int(input("Enter a value: "))
val2 = int(input("Enter a new value: "))
op = input("Enter an operator (+, -, *, /): ")

if op == "+":
    result = val1 + val2
    print(result)
elif op == "-":
    result = val1 - val2
    print(result)
elif op == "*":
    result = val1 * val2
    print(result)
elif op == "/":
    result = val1 / val2
    print(round(result), 2)
else:
    print(f"{op} is not a valid operator")