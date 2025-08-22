import random

def spin_row():
    symbols = ['🍒', '🍉', '🍇', '🔔', '⭐']
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍇':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 5
        elif row[0] == '⭐':
            return bet * 10
    return 0

def main():
    balance = 100

    print("Welcome to the Slot Machine!")
    print(f"Your starting balance is: ${balance}")
    while balance > 0:
        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number for your bet.")
            continue 

        bet = int(bet)

        if bet > balance:
            print("You cannot bet more than your current balance.")
            continue
        
        if bet <= 0:
            print("Please enter a bet greater than 0.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning the slot machine...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
            balance += payout  
        else:
            print("You lost this round.")

        print(f"Your current balance is: ${balance}\n")
        if balance <= 0:
            print("You have run out of money. Game over!")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == 'y':
                balance = 100
                print(f"Your new starting balance is: ${balance}")
            else:
                break
        


if __name__ == "__main__":
    main()