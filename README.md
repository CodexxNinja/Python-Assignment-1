# Python Control Flow: A Detailed Guide

![Python Sticker](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Logic Sticker](https://img.shields.io/badge/Logic-Conditionals-orange?style=flat-square) ![Iteration Sticker](https://img.shields.io/badge/Iteration-Loops-yellow?style=flat-square)

## Overview
In programming, "Control Flow" refers to the order in which individual statements and instructions are executed or evaluated. By default, a Python script runs line-by-line from top to bottom. Control flow statements—specifically **Conditionals** and **Loops**—allow you to change that default behavior so your program can make decisions, skip lines, or repeat actions automatically.

---

## 1. Conditional Statements (`if`, `elif`, `else`)

### What are they?
Conditional statements are the decision-makers of your program. They act like a **fork in the road**, allowing your code to respond differently depending on the situation (e.g., user input, data values, or application state).

### How do they work?
They evaluate an expression to see if it is mathematically or logically `True` or `False`. 
* **`if`:** The starting point. The program asks a question. If the answer is `True`, it runs the indented block of code directly below it. If `False`, it skips it.
* **`elif` (Else-If):** The alternative. If the initial `if` statement is `False`, the program checks this next condition. You can have as many `elif` statements as you need to check multiple specific scenarios.
* **`else`:** The catch-all backup plan. It does not evaluate a condition. It simply catches anything that evaluated to `False` in the `if` and `elif` blocks above it.

### Code Example:
```python
user_age = 20

if user_age >= 65:
    # Runs ONLY if age is 65 or older
    print("Eligible for senior discount.")
elif user_age >= 18:
    # Runs ONLY if the 'if' was False, AND age is 18 to 64
    print("Standard adult ticket price.")
else:
    # Runs ONLY if all the above were False (under 18)
    print("Eligible for child discount.")

# Python-Assignment-1: Iteration & Cryptography

![Python Sticker](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Security Sticker](https://img.shields.io/badge/RSA%20%26%20Hashlib-Security-blue?style=for-the-badge) ![Iteration Sticker](https://img.shields.io/badge/Iteration-Loops-yellow?style=for-the-badge)

<pre>
  _____       _   _                  
 |  __ \     | | | |                 
 | |__) |   _| |_| |__   ___  _ __   
 |  ___/ | | | __| '_ \ / _ \| '_ \  
 | |   | |_| | |_| | | | (_) | | | | 
 |_|    \__, |\__|_| |_|\___/|_| |_| 
         __/ |                       
        |___/                        
</pre>

## Overview
This repository contains the implementation for **Python-Assignment-1**, which applies practical Python programming to system security concepts like RSA key generation and digital certificates. 

A core component of building these scripts involves handling repetitive tasks—such as processing multiple files for hashing, or waiting for valid user input. This documentation serves as an educational reference on how Python handles these repetitive tasks using **Loops**.

---

## The Core Concept: Loops in Python

In programming, we rarely want to write the same line of code multiple times. "Control Flow" allows us to dictate how our program runs. Loops are a specific type of control flow designed for **iteration**—executing a block of code repeatedly until a specific condition is met or a sequence is fully processed.

Python utilizes two primary types of loops: the `for` loop and the `while` loop.

### 1. The `for` Loop
The `for` loop is used for iterating over a known sequence. This sequence could be a list of items, a string of characters, or a specific range of numbers. 

Think of a `for` loop like a teacher handing out exams. The teacher knows exactly how many students are in the classroom, and they will perform the action (handing out a paper) for every single student until the class list is finished.

**Common Use Cases:**
* Processing every item in a dataset.
* Running a mathematical operation a strict, predefined number of times.

**Syntax Example (Iterating over a list):**
```python
# A list of files we need to encrypt
files_to_hash = ["document.txt", "image.png", "data.csv"]

for file in files_to_hash:
    print(f"Applying hashlib to: {file}")


Conversation with Gemini
https://github.com/CodexxNinja/Python-Assignment-1.git. Give Proper Detailed README for this Repo. Don't use emoji use stickers

Since the repository link is currently inaccessible (it may be private, empty, or not yet indexed), I am unable to read the direct source files.

However, I have prepared a comprehensive, properly formatted README template for Python-Assignment-1. The structure below uses a Cryptography and System Security Lab implementation—specifically focusing on digital certificates using RSA and hashlib—as a highly detailed example context.

Please clarify the exact modules or topics covered in your repository if this assignment involves different concepts (such as standard data structures, web APIs, or basic scripting), and I will update the technical sections immediately based on your missing details.

Python-Assignment-1
(Text Sticker: Python Logo Outline)

Overview
This repository contains the implementation for Python-Assignment-1, structured as an experiential learning activity. The codebase focuses on applying core cryptographic concepts, specifically the generation and verification of digital certificates.

By bridging theoretical system security concepts with practical Python programming, this project demonstrates how modern cryptographic standards ensure data integrity and user authenticity.

Key Features
Key Generation: Utilizes the RSA algorithm to generate secure public and private key pairs.

Data Hashing: Implements the hashlib library to create secure digests of file contents or strings, ensuring data integrity.

Digital Certificates: Simulates the creation, signing, and verification process of digital certificates.

Interactive CLI: Provides a clear command-line interface for users to test encryption workflows seamlessly.

Tech Stack
Language: Python 3.x

Core Libraries: rsa, hashlib

Version Control: Git

Directory Structure
Plaintext
Python-Assignment-1/
├── src/
│   ├── key_generator.py      
│   ├── certificate_gen.py    
│   └── verifier.py           
├── tests/
│   └── test_crypto.py
├── requirements.txt
└── README.md
Installation & Setup
Clone the repository:

Bash
git clone https://github.com/CodexxNinja/Python-Assignment-1.git
cd Python-Assignment-1
Environment Recovery (If needed):
If you need to revert to the base assignment state at any point during your development, utilize Git's hard reset to sync with the main branch:

Bash
git reset --hard origin/main
Set up a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Usage
Run the primary script to execute the digital certificate lifecycle:

Bash
python src/certificate_gen.py
(Note: Follow the terminal prompts to input the required text or file paths for hashing and signing).

Academic Context
This assignment aligns with Semester VI Computer Science and Engineering (AIML) curricula. It fulfills practical requirements for Cryptography and System Security labs, aiming to bridge the gap between algorithmic academic theory and industry-ready software development practices.

Author
GitHub: CodexxNinja

In README Explain Python Conditional Statements for and while loop in detail

Here is a detailed section you can append directly to your README.md file. It maintains the professional aesthetic with markdown badges (stickers) and breaks down the logic clearly for anyone reviewing your repository.

Markdown
## Python Control Flow: Conditionals and Loops

![Logic Sticker](https://img.shields.io/badge/Logic-Conditionals-orange?style=flat-square) ![Iteration Sticker](https://img.shields.io/badge/Iteration-Loops-yellow?style=flat-square)

Control flow statements are the backbone of decision-making and repetition in Python. They allow the program to dynamically respond to different inputs and automate repetitive tasks without rewriting code.

### 1. Conditional Statements (`if`, `elif`, `else`)
Conditional statements evaluate a boolean expression (True or False) and execute a block of code only if the condition is met. 

* **`if` statement:** The starting point. If the condition is True, its code block runs.
* **`elif` (else if):** Used to check multiple conditions sequentially if the initial `if` statement is False. You can have as many `elif` blocks as needed.
* **`else`:** The fallback execution block. It runs if all preceding `if` and `elif` conditions evaluate to False.

**Syntax Example:**
```python
user_role = "admin"

if user_role == "admin":
    print("Access granted to the dashboard.")
elif user_role == "guest":
    print("Limited access granted.")
else:
    print("Access denied.")
2. The for Loop
A for loop in Python is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string). Unlike traditional C-style for loops that rely on counter variables, Python's for loop behaves more like an iterator method, grabbing each item in the sequence one by one.

Common use cases:

Traversing data structures.

Executing a block of code a specific number of times using the range() function.

Syntax Example (Iterating over a list):

Python
authorized_users = ["Alice", "Bob", "Charlie"]

for user in authorized_users:
    print(f"Checking permissions for {user}...")
Syntax Example (Using range):

Python
# This loop will run 5 times (0 through 4)
for i in range(5):
    print(f"Processing batch {i}")
3. The while Loop
A while loop executes a set of statements continuously as long as a specified condition remains True. It is highly useful when you do not know beforehand how many times the loop needs to run (e.g., waiting for a user to input a valid response or polling a server state).

Caution: You must ensure that the condition eventually becomes False within the loop's block; otherwise, you will create an "infinite loop" that crashes the program.

Syntax Example:

Python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Login attempt {attempts + 1}")
    attempts += 1  # Crucial: update the condition variable

print("Maximum attempts reached.")
4. Loop Control Statements
To give you even finer control over your iteration, Python provides three essential loop control keywords:

break: Instantly terminates the loop entirely, skipping any remaining iterations.

continue: Skips the rest of the current iteration and instantly jumps back to the top of the loop to evaluate the next item or condition.

pass: A null operation. It does nothing and is typically used as a placeholder in code blocks where a statement is syntactically required but no action is needed yet.

Give full one README

Here is the complete, unified README.md file. You can copy the entire block below and paste it directly into your repository.

Markdown
# Python-Assignment-1 

![Python Sticker](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Security Sticker](https://img.shields.io/badge/RSA%20%26%20Hashlib-Security-blue?style=for-the-badge) ![Academic Sticker](https://img.shields.io/badge/Lab-Experiential%20Learning-green?style=for-the-badge)

<pre>
  _____       _   _                  
 |  __ \     | | | |                 
 | |__) |   _| |_| |__   ___  _ __   
 |  ___/ | | | __| '_ \ / _ \| '_ \  
 | |   | |_| | |_| | | | (_) | | | | 
 |_|    \__, |\__|_| |_|\___/|_| |_| 
         __/ |                       
        |___/                        
</pre>

## Overview
This repository contains the implementation for **Python-Assignment-1**, structured as an experiential learning activity. The codebase focuses on applying core cryptographic concepts, specifically the generation and verification of digital certificates. 

By bridging theoretical system security concepts with practical Python programming, this project demonstrates how modern cryptographic standards ensure data integrity and user authenticity.

## Key Features
* **Key Generation:** Utilizes the RSA algorithm to generate secure public and private key pairs.
* **Data Hashing:** Implements the `hashlib` library to create secure digests of file contents or strings, ensuring data integrity.
* **Digital Certificates:** Simulates the creation, signing, and verification process of digital certificates.
* **Interactive CLI:** Provides a clear command-line interface for users to test encryption workflows seamlessly.

## Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** `rsa`, `hashlib`
* **Version Control:** Git

## Directory Structure
```text
Python-Assignment-1/
├── src/
│   ├── key_generator.py      
│   ├── certificate_gen.py    
│   └── verifier.py           
├── tests/
│   └── test_crypto.py
├── requirements.txt
└── README.md
Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/CodexxNinja/Python-Assignment-1.git](https://github.com/CodexxNinja/Python-Assignment-1.git)
cd Python-Assignment-1
Environment Recovery (If needed):
If you need to revert to the base assignment state at any point during your development, utilize Git's hard reset to sync with the main branch:

Bash
git reset --hard origin/main
Set up a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Usage
Run the primary script to execute the digital certificate lifecycle:

Bash
python src/certificate_gen.py
(Note: Follow the terminal prompts to input the required text or file paths for hashing and signing).

Educational Reference: Python Control Flow
Control flow statements are the backbone of decision-making and repetition in Python. They allow the program to dynamically respond to different inputs and automate repetitive tasks without rewriting code.

1. Conditional Statements (if, elif, else)
Conditional statements evaluate a boolean expression (True or False) and execute a block of code only if the condition is met.

if statement: The starting point. If the condition is True, its code block runs.

elif (else if): Used to check multiple conditions sequentially if the initial if statement is False. You can have as many elif blocks as needed.

else: The fallback execution block. It runs if all preceding if and elif conditions evaluate to False.

Syntax Example:

Python
user_role = "admin"

if user_role == "admin":
    print("Access granted to the dashboard.")
elif user_role == "guest":
    print("Limited access granted.")
else:
    print("Access denied.")
2. The for Loop
A for loop in Python is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string). Unlike traditional C-style for loops that rely on counter variables, Python's for loop behaves more like an iterator method, grabbing each item in the sequence one by one.

Common use cases:

Traversing data structures.

Executing a block of code a specific number of times using the range() function.

Syntax Example (Iterating over a list):

Python
authorized_users = ["Alice", "Bob", "Charlie"]

for user in authorized_users:
    print(f"Checking permissions for {user}...")
Syntax Example (Using range):

Python
# This loop will run 5 times (0 through 4)
for i in range(5):
    print(f"Processing batch {i}")
3. The while Loop
A while loop executes a set of statements continuously as long as a specified condition remains True. It is highly useful when you do not know beforehand how many times the loop needs to run (e.g., waiting for a user to input a valid response or polling a server state).

Caution: You must ensure that the condition eventually becomes False within the loop's block; otherwise, you will create an "infinite loop" that crashes the program.

Syntax Example:

Python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Login attempt {attempts + 1}")
    attempts += 1  # Crucial: update the condition variable

print("Maximum attempts reached.")
4. Loop Control Statements
To give you even finer control over your iteration, Python provides three essential loop control keywords:

break: Instantly terminates the loop entirely, skipping any remaining iterations.

continue: Skips the rest of the current iteration and instantly jumps back to the top of the loop to evaluate the next item or condition.

pass: A null operation. It does nothing and is typically used as a placeholder in code blocks where a statement is syntactically required but no action is needed yet.

Academic Context
This assignment fulfills practical requirements for Cryptography and System Security labs, aiming to bridge the gap between algorithmic academic theory and industry-ready software development practices.

Author
GitHub: CodexxNinja

Give Everything in README File to copy paste

Markdown
# Python-Assignment-1 

![Python Sticker](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Security Sticker](https://img.shields.io/badge/RSA%20%26%20Hashlib-Security-blue?style=for-the-badge) ![Academic Sticker](https://img.shields.io/badge/Lab-Experiential%20Learning-green?style=for-the-badge)

<pre>
  _____       _   _                  
 |  __ \     | | | |                 
 | |__) |   _| |_| |__   ___  _ __   
 |  ___/ | | | __| '_ \ / _ \| '_ \  
 | |   | |_| | |_| | | | (_) | | | | 
 |_|    \__, |\__|_| |_|\___/|_| |_| 
         __/ |                       
        |___/                        
</pre>

## Overview
This repository contains the implementation for **Python-Assignment-1**, structured as an experiential learning activity. The codebase focuses on applying core cryptographic concepts, specifically the generation and verification of digital certificates. 

By bridging theoretical system security concepts with practical Python programming, this project demonstrates how modern cryptographic standards ensure data integrity and user authenticity.

## Key Features
* **Key Generation:** Utilizes the RSA algorithm to generate secure public and private key pairs.
* **Data Hashing:** Implements the `hashlib` library to create secure digests of file contents or strings, ensuring data integrity.
* **Digital Certificates:** Simulates the creation, signing, and verification process of digital certificates.
* **Interactive CLI:** Provides a clear command-line interface for users to test encryption workflows seamlessly.

## Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** `rsa`, `hashlib`
* **Version Control:** Git

## Directory Structure
```text
Python-Assignment-1/
├── src/
│   ├── key_generator.py      
│   ├── certificate_gen.py    
│   └── verifier.py           
├── tests/
│   └── test_crypto.py
├── requirements.txt
└── README.md
Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/CodexxNinja/Python-Assignment-1.git](https://github.com/CodexxNinja/Python-Assignment-1.git)
cd Python-Assignment-1
Environment Recovery (If needed):
If you need to revert to the base assignment state at any point during your development, utilize Git's hard reset to sync with the main branch:

Bash
git reset --hard origin/main
Set up a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Usage
Run the primary script to execute the digital certificate lifecycle:

Bash
python src/certificate_gen.py
(Note: Follow the terminal prompts to input the required text or file paths for hashing and signing).

Educational Reference: Python Control Flow
Control flow statements are the backbone of decision-making and repetition in Python. They allow the program to dynamically respond to different inputs and automate repetitive tasks without rewriting code.

1. Conditional Statements (if, elif, else)
Conditional statements evaluate a boolean expression (True or False) and execute a block of code only if the condition is met.

if statement: The starting point. If the condition is True, its code block runs.

elif (else if): Used to check multiple conditions sequentially if the initial if statement is False. You can have as many elif blocks as needed.

else: The fallback execution block. It runs if all preceding if and elif conditions evaluate to False.

Syntax Example:

Python
user_role = "admin"

if user_role == "admin":
    print("Access granted to the dashboard.")
elif user_role == "guest":
    print("Limited access granted.")
else:
    print("Access denied.")
2. The for Loop
A for loop in Python is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string). Unlike traditional C-style for loops that rely on counter variables, Python's for loop behaves more like an iterator method, grabbing each item in the sequence one by one.

Common use cases:

Traversing data structures.

Executing a block of code a specific number of times using the range() function.

Syntax Example (Iterating over a list):

Python
authorized_users = ["Alice", "Bob", "Charlie"]

for user in authorized_users:
    print(f"Checking permissions for {user}...")
Syntax Example (Using range):

Python
# This loop will run 5 times (0 through 4)
for i in range(5):
    print(f"Processing batch {i}")
3. The while Loop
A while loop executes a set of statements continuously as long as a specified condition remains True. It is highly useful when you do not know beforehand how many times the loop needs to run (e.g., waiting for a user to input a valid response or polling a server state).

Caution: You must ensure that the condition eventually becomes False within the loop's block; otherwise, you will create an "infinite loop" that crashes the program.

Syntax Example:

Python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Login attempt {attempts + 1}")
    attempts += 1  # Crucial: update the condition variable

print("Maximum attempts reached.")
4. Loop Control Statements
To give you even finer control over your iteration, Python provides three essential loop control keywords:

break: Instantly terminates the loop entirely, skipping any remaining iterations.

continue: Skips the rest of the current iteration and instantly jumps back to the top of the loop to evaluate the next item or condition.

pass: A null operation. It does nothing and is typically used as a placeholder in code blocks where a statement is syntactically required but no action is needed yet.

Academic Context
This assignment fulfills practical requirements for Cryptography and System Security labs, aiming to bridge the gap between algorithmic academic theory and industry-ready software development practices.

Author
GitHub: CodexxNinja

No Exaplain These Concepts So I will put that in readme

You stopped this response
No Exaplain These Concepts So I will put that in readme

It is great that you want to fully understand the code you are putting into your repository. Grasping these concepts will make writing your own scripts much easier.

Here is a plain-English explanation of how Python control flow works. Think of your code as a train moving down a track. Control flow statements are the switches and loops on those tracks that tell the train where to go.

1. Conditional Statements (if, elif, else)
Think of conditionals as a fork in the road. The program asks a yes-or-no question (a boolean condition). Depending on the answer, it takes a specific path.

if: The first question. "Is it raining?" If yes, grab an umbrella (run this block of code). If no, skip it.

elif (else if): The follow-up question. "Okay, it's not raining, but is it snowing?" If yes, grab a coat. You can ask as many elif questions as you want.

else: The default backup plan. "It's not raining and it's not snowing. I guess I'll just wear a t-shirt." This runs when everything above it is false.

2. The for Loop
Think of a for loop as dealing a deck of cards. You have a specific collection of items (like a list of names or numbers), and you want to do something with each one, one by one, until the deck is empty.

