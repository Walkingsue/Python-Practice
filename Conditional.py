num = 8
a = 3
b = 5
age = 17
weather = 18
user_role = "admin"

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)
max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)
status = "Adult" if age >= 18 else "Minor"
print(status)
temp =  "HOT AF" if weather >= 30 else "Fresco"
print(temp)
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)