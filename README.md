```markdown
# 🚀 Codveda Internship – Technologies Repository

This repository contains all the **projects, tasks, and experiments** completed during my internship at **Codveda Technologies**.  
The work reflects my learning progress, problem-solving skills, and practical application of programming concepts using **Python and related technologies**.

---

## 📌 Purpose of This Repository

The goal of this repository is to:

* Demonstrate hands-on experience gained during the Codveda internship
* Apply theoretical concepts to real-world programming tasks
* Write clean, readable, and maintainable code
* Improve problem-solving, debugging, and software design skills

---

## 🛠️ Technologies Used

* **Python 3**
* Standard Python Libraries (`os`, `requests`, `json`, `random`, `typing`, etc.)
* File handling & persistence
* Command-Line Interface (CLI) applications
* Basic security concepts (hashing, encryption)
* Backtracking algorithms

---

## 📂 Repository Structure

```

codveda-tech/
(venv) (base) bode-murairi@bode-murairi-HP-ProBook-450-15-6-inch-G10-Notebook-PC:~/Documents/work/codveda_tech$ tree
.
├── advanced
│   ├── encryption
│   │   ├── file_encrypt.py
│   │   └── file.txt
│   └── n_queen
│       ├── __init__.py
│       └── main.py
├── basic
│   ├── calculator
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── project.md
│   │   └── users.txt
│   ├── number_guessing
│   │   ├── __init__.py
│   │   ├── number_guessing.py
│   │   └── score.txt
│   └── word_counter
│       ├── file.txt
│       ├── __init__.py
│       └── word_counter.py
├── intermediate
│   ├── todo_list
│   │   ├── __init__.py
│   │   └── todo.py
│   ├── weather_api
│   │   ├── INSTRUCTIONS.md
│   │   └── main.py
│   └── web_scraper
│       ├── __init__.py
│       ├── README.md
│       └── web_scraper.py
├── README.md
├── requirements.txt

````

**Legend:**

- 🟢 Basic Projects – beginner-level CLI tasks  
- 🟡 Intermediate Projects – moderate complexity, API usage, JSON persistence  
- 🔴 Advanced Projects – algorithms, encryption, backtracking  
- 🖩 Calculator, 🎯 Number Guessing, 📄 Word Counter  
- ✅ To-Do List, 🌦 Weather API, 🌐 Web Scraper  
- 🔐 File Encryption, ♛ N-Queens Solver  

---

## 📌 Project Details

### 1️⃣ Basic Projects

**Calculator** (`basic/calculator`) 🖩  
- CLI calculator with per-user authentication  
- Supports +, −, ×, ÷ operations  
- Stores calculation history per user in `users.txt`  
- Password hashing using SHA-256  
- Undo/clear functionality  

**Number Guessing Game** (`basic/number_guessing`) 🎯  
- Guess a random number between 1 and 100  
- Maximum of 3 trials per round  
- Scores saved per session and leaderboard maintained in `score.txt`  

**Word Counter** (`basic/word_counter`) 📄  
- Counts words in a given text file  
- Demonstrates file reading and string manipulation  

---

### 2️⃣ Intermediate Projects

**To-Do List** (`intermediate/todo_list`) ✅  
- CLI task manager  
- Add, delete, mark as done, and list tasks  
- Tasks stored in JSON file  
- Error handling for invalid inputs  

**Weather API CLI** (`intermediate/weather_api`) 🌦  
- Fetches live weather data for any city  
- Displays temperature, humidity, wind speed, pressure, cloud cover, and more  
- **Requires API key from [WeatherAPI](https://www.weatherapi.com/)**  
- Steps:  
  1. Sign up and generate your API key on WeatherAPI  
  2. Create a `.env` file in the project folder:  
     ```
     WEATHER_API_KEY=your_api_key_here
     ```  
  3. Run the script:  
     ```bash
     python main.py
     ```  

**Web Scraper** (`intermediate/web_scraper`) 🌐  
- Scrapes data from websites  
- Demonstrates HTML parsing and data extraction  

---

### 3️⃣ Advanced Projects

**File Encryption/Decryption** (`advanced/encryption`) 🔐  
- Encrypts/decrypts text files using **Caesar Cipher**  
- Saves encrypted files with `.enc` extension  
- Decrypted files saved with `.dec` extension  
- CLI menu for easy operation  

**N-Queens Problem Solver** (`advanced/n_queen`) ♛  
- Solves the classic N-Queens problem using **backtracking**  
- Displays solutions in a clear ASCII board format  
- Allows user input for N (board size)  
- Demonstrates recursive algorithms and constraint checking  

---

## ▶️ How to Run a Project

1. Clone the repository:

```bash
git clone https://github.com/BodeMurairi/codveda_tech.git
````

2. Navigate to the project folder:

```bash
cd basic/calculator
```

3. Run the program:

```bash
python3 main.py
```

> Replace `main.py` with the relevant script for the project you want to run.

---

## Skills Demonstrated

* Python fundamentals and advanced syntax
* CLI development
* File I/O and persistence (JSON, TXT)
* Recursion & backtracking algorithms
* Error handling and validation
* Modular code and project organization
* Basic security concepts (password hashing, encryption)

---

## Future Improvements

* Add unit tests for all projects
* Upgrade encryption project to use **Fernet** (real cryptography)
* Add GUI or web-based interfaces
* Migrate file-based storage to a database
* Implement multi-solution display for N-Queens

---

## Author

**Bode Murairi**
Software Engineering Student
Codveda Technologies – Intern

```
