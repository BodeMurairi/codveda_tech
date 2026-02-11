
---

# 🧮 Secure CLI Calculator with User Authentication

A command-line calculator built in **Python** that goes beyond basic arithmetic by introducing **user authentication**, **secure password hashing**, **calculation history**, **state reuse**, and **file persistence**.

This project was designed to demonstrate **clean code structure**, **error handling**, and **security-aware thinking** in a simple but realistic application.

---

## 🚀 Features

### ✅ Core Calculator

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*` or `x`)
* Division (`/`) with division-by-zero protection

### 🔁 Reuse Last Result

* Use `ANS` to reuse the previous calculation result
* Can be used as:

  * First value
  * Second value
  * Both values

### 🧾 Calculation History

* View calculation history (`h`)
* Undo last calculation (`u`)
* Clear history (`c`)
* History persists between sessions

### 👤 User Authentication

* Username-based login
* Passwords are **hashed using SHA-256**
* No plaintext passwords stored
* Automatic account creation for new users

### 🔐 User Isolation

* Each user has:

  * Their own encrypted password entry
  * Their own calculation history file
* History is loaded automatically on login

### 📂 File Persistence

* `users.txt` → stores usernames and hashed passwords
* `{username}_history.txt` → stores calculation history per user

---

## 🛠️ Technologies Used

* **Python 3.10+**
* `hashlib` (for password hashing)
* `os` (file handling)
* `typing` (type hints)

---

## 📦 Project Structure

```
.
├── calculator.py
├── users.txt
├── username_history.txt
└── README.md
```

---

## ▶️ How to Run

1. Clone or download the project
2. Ensure Python 3.10+ is installed
3. Run the script:

```bash
python3 calculator.py
```

---

## 🔑 Authentication Flow

1. Enter a username
2. Enter a password
3. If user exists:

   * Password is verified using SHA-256 hash comparison
4. If user does not exist:

   * Account is automatically created
   * Password is securely stored as a hash

---

## 🧠 Example Usage

```text
Choose an operation: +
Enter the first value: 10
Enter the second value: 5
Result: 15

Choose an operation: *
Enter the first value: ANS
Enter the second value: 2
Result: 30
```

---

## 🧪 Error Handling

* Invalid numeric inputs
* Invalid operations
* Division by zero
* Attempting to use `ANS` with no previous result
* Incorrect password login

All errors are handled gracefully with clear messages.

---

## 🔒 Security Notes

* Passwords are **never stored in plaintext**
* SHA-256 hashing is used for simplicity
* Each user’s data is isolated in separate files

> ⚠️ This is an educational project and not intended for production authentication systems.

---

## 🎯 Learning Objectives Demonstrated

* Modular function design
* Type hinting with `Union[int, float]`
* Pattern matching (`match-case`)
* Secure password handling
* File-based persistence
* State management in CLI applications
* Clean error handling

---

## 📌 Possible Future Improvements

* Password salting
* Encrypted history files
* Unit tests
* Logging system
* Transition to a database backend
* GUI or web interface

---

## 🧑‍💻 Author

**Bode Murairi**
Software Engineering Student
Aspiring Backend & AI Engineer
b.murairi@alustudent.com/bodemurairi2@gmail.com
---
