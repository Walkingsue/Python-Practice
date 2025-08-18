Question = ("How old is the League of legends? ", "What is the biggest cat species? ",
 "What is 2 + 2? ", "What is the capital of Japan? ")

options = (
("A. 20", "B. 29", "C. 30", "D. 27"), 
("A. Persa", "B. Mainecoon", "C. Belga", "D. Siberian"),
("A. 4", "B. 3", "C. 5", "D. 6"), 
("A. Okinawa", "B. Osaka", "C. Kyoto", "D. Tokyo"))

answer = ("B", "B", "A", "D")

guesses = [] 

score = 0

quest_num = 0

for question in Question:
    print("--------------------------------------------------------------")
    print(question)
    for option in options[quest_num]:
        print(option)
    guess = input("Enter A, B, C or D: ").upper()
    guesses.append(guess)
    if guess == answer[quest_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was " + answer[quest_num])
    quest_num += 1

print("--------------------------------------------------------------")
print("                         RESULTS                                ")
print("--------------------------------------------------------------")

for answer in answer:
    print(answer, end=" ")
    
print()

for guess in guesses:
    print(guess, end=" ")
print()

score = int((score / len(Question)) * 100)
print("Your score is " + str(score) + "%")