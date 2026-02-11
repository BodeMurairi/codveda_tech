#!/usr/bin/env python3

import os
import getpass
import hashlib
from typing import Union

Number = Union[int, float]

# Calculator functions
def addition(a: Number, b: Number) -> Number:
    """
    Addition function
    
    :param a: Description
    :type a: Number
    :param b: Description
    :type b: Number
    :return: Description
    :rtype: Number
    """
    return a + b

def subtraction(a: Number, b: Number) -> Number:
    """
    Subtraction function
    
    :param a: Description
    :type a: Number
    :param b: Description
    :type b: Number
    :return: Description
    :rtype: Number
    """
    return a - b

def multiplication(a: Number, b: Number) -> Number:
    """
    Multiplication function
    
    :param a: Description
    :type a: Number
    :param b: Description
    :type b: Number
    :return: Description
    :rtype: Number
    """
    return a * b

def division(a: Number, b: Number) -> Number:
    """
    Division function
    
    :param a: Description
    :type a: Number
    :param b: Description
    :type b: Number
    :return: Description
    :rtype: Number
    """
    if b == 0:
        raise ValueError("Division by 0 is not allowed")
    return a / b

def get_number(prompt: str, last_result: Number = None) -> Number:
    """Get a number from the user. 
    Use last_result if user enters 'ANS'.
    """
    user_input = input(prompt)
    if user_input.strip().upper() == "ANS":
        if last_result is None:
            raise ValueError("No previous result to reuse")
        return last_result
    try:
        return float(user_input)
    except ValueError:
        raise ValueError("Enter a valid number")

# authentication
def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user():
    """Authenticate users"""
    users_file = "users.txt"
    if not os.path.exists(users_file):
        open(users_file, "w").close()

    username = input("Enter your username: ").strip().lower()
    password = getpass.getpass("Enter your password: ")
    password_hash = hash_password(password)

    # Load existing users
    users = {}
    with open(users_file, "r") as file:
        for line in file:
            if ":" in line:
                user, pwd_hash = line.strip().split(":", 1)
                users[user] = pwd_hash

    # Existing user login
    if username in users:
        if users[username] == password_hash:
            print(f"Welcome back {username.upper()}!")
        else:
            print("Incorrect password. Exiting...")
            exit()
    else:
        # Register new user
        print("New user! Creating account...")
        users[username] = password_hash
        with open(users_file, "a") as file:
            file.write(f"{username}:{password_hash}\n")
        print(f"Account created. Welcome {username.upper()}!")

    return username

if __name__ == "__main__":
    username = authenticate_user()
    history_file = f"{username}_history.txt"
    history = []
    last_result = None

    # Load previous history if exists
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = [line.strip() for line in file.readlines()]
        if history:
            last_result = float(history[-1].split("=")[-1].strip())

    while True:
        print("""
    Choose an operation (+, -, x, /)
    Other options:
        h -> show history
        u -> undo last calculation
        c -> clear history
        q -> quit
    You can type 'ANS' for numbers to reuse the last result.Select an operation then type ANS on the first or second or both
    """
              )

        user_choice = input("Choose an operation: ").lower()

        if user_choice == "q":
            print("Thanks for using the calculator!")
            break
        elif user_choice == "h":
            if not history:
                print("No calculations yet.")
            else:
                print("Calculation history:")
                for entry in history:
                    print(entry)
            continue
        elif user_choice == "u":
            if history:
                removed = history.pop()
                print(f"Removed last calculation: {removed}")
                with open(history_file, "w") as file:
                    file.write("\n".join(history) + ("\n" if history else ""))
                last_result = float(history[-1].split("=")[-1].strip()) if history else None
            else:
                print("No calculation to undo.")
            continue
        elif user_choice == "c":
            history = []
            last_result = None
            open(history_file, "w").close()
            print("History cleared.")
            continue
        elif user_choice not in ["+", "-", "*", "x", "/"]:
            print("Invalid operation. Try again.")
            continue

        try:
            a = get_number("Enter the first value: ", last_result)
            b = get_number("Enter the second value: ", last_result)

            match user_choice:
                case "+":
                    result = addition(a, b)
                    operation_result = f"{a} + {b} = {result}"
                case "-":
                    result = subtraction(a, b)
                    operation_result = f"{a} - {b} = {result}"
                case "*" | "x":
                    result = multiplication(a, b)
                    operation_result = f"{a} * {b} = {result}"
                case "/":
                    result = division(a, b)
                    operation_result = f"{a} / {b} = {result}"

            print(f"Result: {result}")
            history.append(operation_result)
            last_result = result

            # Save user history
            with open(history_file, "w") as file:
                file.write("\n".join(history) + "\n")

        except Exception as error:
            print("An error happened:", error)
