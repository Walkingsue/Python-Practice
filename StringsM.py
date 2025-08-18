name = input("Enter your name: ")
print(name.find("l"))
result = name.rfind("e")
print(result)
name = name.lower()
print(name)
name = name.upper()
print(name)
name = name.isalpha()
print(name)
some_w = "1234"
result = some_w.isdigit()
print(result)


user_name = input("Enter your username: ")
if len(user_name) < 5:
    print("Username must be at least 5 characters long.")
elif not user_name.isalpha():
    print("Username must contain only letters.")
elif user_name.rfind(" ") != -1:
    print("Username must not contain spaces.")
else:
    print("Username is valid.")

user_email = input("Enter your email: ")

user = user_email.index("@")
user_name = user_email[:user]
domain = user_email[user + 1:]

print(f"Your email domain is: {domain} and your username is: {user_name}")

