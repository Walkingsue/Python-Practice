balance = 0
is_running = True

def show_balance(balance):
    print(f"Current balance: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: $"))
    if amount < 0:
        print("Deposit amount must be positive.")
        return 0
    else:
        return amount
    

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Withdrawal amount must be positive.")
        return 0
    else:
        return amount 

while is_running:
    choice = int(input("Choose an option: \n1) Show Balance \n2) Deposit \n3) Withdraw \n4) Exit: \n"))

    match choice:
        case 1:
            show_balance(balance)
        case 2:
            balance = float(balance) + deposit()
        case 3:
            balance = float(balance) - withdraw(balance)
        case 4:
            is_running = False
            print("Exiting...")
        case _:
            print("Invalid choice. Please try again.")
