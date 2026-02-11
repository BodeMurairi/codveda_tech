#!/usr/bin/env python3

import random

def main():
    points = 0

    while True:
        number = random.randrange(1, 101)
        trials = int(input("Input number of trials\n"))
        print("\nNew Round Started!")
        print(f"You have {trials} trials to guess the number between 1 and 100.")

        while trials > 0:
            try:
                number_guessed = int(input("Enter a number between 1 and 100: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if number_guessed > number:
                trials -= 1
                print(f"Too high! Trials left: {trials}")

            elif number_guessed < number:
                trials -= 1
                print(f"Too low! Trials left: {trials}")

            else:
                print(f"Correct! The number was {number}")
                points += 1
                print(f"Your current points: {points}")
                break

        if trials == 0:
            print(f"Game Over! The correct number was {number}")

        with open("score.txt", "w") as file:
            file.write(f"Points this session: {points}")

        print("Score saved to score.txt")

if __name__ == "__main__":
    main()
