import random
guess_word = ('python', 'apple', 'hangman')

_art = {0: ("   ",
            "   ",
            "   "),
        1: (" o ",
            "   ",
            "   "),
        2: (" o ",
            " | ",
            "   "),
        3: (" o ",
            "/| ",
            "   "),
        4: (" o ",
            "/|\\",
            "   "),
        5: (" o ",
            "/|\\",
            "/  "),
        6: (" o ",
            "/|\\",
            "/ \\")}

def display_man(wrong_guesses):
    for line in _art[wrong_guesses]:
        print(line)

def display_answer(answer):
    print(" ".join(answer))

def display_hint(hint):
    print(" ".join(hint))

def main():
    answer = random.choice(guess_word)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        user_guess = input("Enter your guess: ").lower()

        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if user_guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
    
        guessed_letters.add(user_guess)


        if user_guess in answer:
            for i in range(len(answer)):
                if answer[i] == user_guess:
                    hint[i] = user_guess
        else:
            wrong_guesses += 1

        if '_' not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("Congratulations! You've guessed the word!")
            is_running = False
        elif wrong_guesses >= len(_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Game Over! You've been hanged.")
            is_running = False




                    
if __name__ == "__main__":
    main()