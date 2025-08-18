import random
choice = ("rock", "paper", "scissors")
score = 0
running = True
while running:
    while True:
    #ask for the player input
        player = input("Pick between Rock, Paper, Scissors: ").lower()
        #get computer choice
        option = random.choice(choice)
        #check if the player input is valid
        if player not in choice:
            print("Invalid choice, please try again.")
            continue
        #check win consditions
        elif player == choice[0] and option == choice[2]:
            print(f"You win! {player} beats {option}")
            score += 1
        elif player == choice[1] and option == choice[1]:
            print(f"You win! {option} beats {player}")
            score += 1
        elif player == choice[2] and option == choice[1]:
            print(f"You win! {player} beats {option}")
            score += 1
        elif player == option:
            print("It's a tie!")
        else:
            print(f"You lose! {option} beats {player}")
            break
        print(f"Your score is {score}")
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        running = False
        print("Thanks for playing!")
