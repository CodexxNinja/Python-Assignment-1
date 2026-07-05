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
