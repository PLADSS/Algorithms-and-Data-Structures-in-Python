import random

def numberGuessGame():
    print("Welcome to the Number Guessing Game!")
    print("Please chose a difficulty level: easy, medium, or hard")
    print("Easy: 10 change , Medium: 5 chances, Hard: 3 chances")
    difficulty = input("Enter your choice: ").lower()
    if difficulty == "easy":
        chances = 10
    elif difficulty == "medium":
        chances = 5
    elif difficulty == "hard":
        chances = 3
    else:
        print("Invalid choice")
        return
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100")
    print(f"You have {chances} chances to guess the number")
    while chances > 0 :
        guess = int(input("Make a guess:"))
        if guess == number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < number:
            print("Too low")
            chances -= 1
        else:
            print("Too high")
            chances -= 1
    if chances == 0:
        print(f"Sorry, you ran out of chances. The number was {number}")

numberGuessGame()