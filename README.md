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
