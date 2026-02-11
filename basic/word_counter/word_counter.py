#!/usr/bin/env python3

filename = "file.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        words = content.split()
        print(f"Number of words: {len(words)}")

except FileNotFoundError:
    print("File not found.")
