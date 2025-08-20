import time

def happy_b():
    return "Happy birthday to you"

print(happy_b())

def count(start, end):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("DONE!")

count(0, 5)

def get_phone(country, area, first, last):
    return f"+{country}-{area}-{first}-{last}"

print(get_phone(first=1234, last=5678, country=1, area=800))


def add(*args): 
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))

def shipping_address(*args, **kwargs):
    for arg in args:
        print(arg, end='')
        print()

    if "apts" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apts')}")

    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_address(
    "John",
    "Doe",
    street="123 Main St",
    apts="Apt 4B",
    city="New York",
    state="NY",
    zip="10001"
)