# CCS 1312 – Assignment 2: User Info & Expense Tracker

A small Python console program that collects basic user information, cleans it up, and then finds the highest and lowest expense among four months.

## What the program does

### Part 1 – User information (`Info` function)
Prompts the user for:
- **Name** – converted to uppercase and stripped of extra spaces
- **Age** – converted from a string to an integer
- **Email** – converted to lowercase and stripped of extra spaces

It then prints the cleaned name, age, email, and the number of characters in the name.

### Part 2 – Expenses (`Expenses` function)
Prompts for expenses for four months (**JAN, FEB, MAR, APR**), stores them in a list, and loops through the list to find:
- the **maximum** expense
- the **minimum** expense

Both values are printed at the end.

## Concepts practiced
- `input()` and type conversion (`int()`)
- String methods: `.upper()`, `.lower()`, `.strip()`, `len()`
- Functions with parameters and multiple return values
- Lists and `for` loops with `range()`
- f-strings and formatted output

## How to run
```bash
python CCS-1312_Assignment-2.py
```
Requires Python 3.9 or newer.

## Example session
```
==================== Welcome ====================
Enter your name:  sara
Enter your age: 20
Enter your email: Sara@Example.COM

Your name is: SARA
Your age is: 20
Your email is: sara@example.com
The number of letters in your name is : 4
==================================================

Enter your JAN expenses: 300
Enter your FEB expenses: 450
Enter your MAR expenses: 200
Enter your APR expenses: 500
```

## Known limitations / possible improvements
- The maximum and minimum are printed inside `{ }` (e.g. `{500}`) because they are wrapped in curly braces inside the f-string/print call.
- `Expenses` reads the global `List` instead of its own `Lst` parameter, and the call passes `list[0]` (the built-in type) rather than a real value; the function overrides these anyway, but it should be cleaned up.
- The name/age/email prompts live inside `Info`, so its `Name` parameter is not actually used.
- No input validation: non-numeric age or expense values will raise a `ValueError`.
