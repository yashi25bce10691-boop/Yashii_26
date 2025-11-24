# ***Personal Expense Tracker – Python Project***

## **📝 Overview**

The Personal Expense Tracker is a simple, console-based Python application that helps users record and monitor their daily spending.
It allows users to add expenses, categorize them, view all expenses, filter by category, and calculate total expenditure.
All data is stored in a JSON file, so expenses are saved even after closing the program.

This project is created as part of the Python Programming course.

## 🚀 Features

### ✔ Add new expense

Allows users to enter amount, category, and note.

### ✔ View all expenses

Displays all recorded expenses in a clean format.

### ✔ Filter by category

Shows only the expenses belonging to a chosen category.

### ✔ Total expenditure

Calculates the overall spending amount.

## 🛠 Technology Used

✦ Python 3

✦ JSON file handling

## ▶ How to Run the Project

### ➟ Step 1: Install Python

Make sure Python 3 is installed.

Check by running:

``` 
python --version
```

### ➟ Step 2: Open Terminal in Project Folder

In VS Code:

```
python src/main.py
```

### ➟ Step 3: Use the Menu

Example:

```
====== EXPENSE TRACKER ======
1. Add Expense
2. View All Expenses
3. Filter by Category
4. Total Expenditure
5. Exit 
```

## ✅ Instructions for Testing the Project:

This section explains how to test all features of the Personal Expense Tracker to ensure that the program works correctly.

### 👉 1. Launch the Application

Open the project folder in VS Code.

Open the terminal in VS Code.

Run the following command:

```
python src/main.py
```


The main menu should appear.

### 👉 2. Test: Add an Expense

From the menu, press 1.

Enter:

Amount (e.g., 200)

Category (e.g., Food)

Note (e.g., Burger)

A message “Expense saved!” should appear.

Confirm that the data is stored in expenses.json.

### 👉 3. Test: View All Expenses

From the main menu, press 2.

The program should display a list of all added expenses in this format:

```
1. ₹200 | Food | Burger
```

Verify that the displayed expenses match the entries inside expenses.json.

### 👉 4. Test: Filter Expenses by Category

From the main menu, press 3.

Enter a category (e.g., Food).

The program should display only the expenses that belong to that category.

Check that the results match the expenses stored in the file.

### 👉 5. Test: Total Expenditure

From the menu, press 4.

The program should calculate the sum of all expenses.

Verify that the displayed total is correct based on the stored values.

### 👉 6. Test: Application Exit

Press 5 to exit.

The program should display a friendly exit message and close without errors.

### 👉 7. Data Persistence Test

Close the program completely.

Run it again using:

```
python src/main.py
```

Press 2 (View All Expenses).

All previously saved expenses should still appear.

This confirms that JSON storage is working properly.

## 🎯 Expected Result

All menu options should function correctly.

No errors should appear during input or output.

Data should remain saved in expenses.json even after restarting the program.

## 🖼 Screenshots

<img width="320" height="159" alt="image" src="https://github.com/user-attachments/assets/a37bfb70-b9ca-4cc5-b3f3-ba5d0ba02127" />



<img width="391" height="115" alt="image" src="https://github.com/user-attachments/assets/a064c6ce-46a8-4725-b6c8-b35da47bac7d" />



<img width="292" height="78" alt="image" src="https://github.com/user-attachments/assets/aec77335-8662-4a81-bfff-ed7a237d6f5b" />



<img width="257" height="74" alt="image" src="https://github.com/user-attachments/assets/1a41ed82-7103-4ef5-b8ec-19076b6dfbb6" />



<img width="235" height="54" alt="image" src="https://github.com/user-attachments/assets/6d2c5754-5cc2-4e59-84bd-c1431514bc11" />



<img width="211" height="45" alt="image" src="https://github.com/user-attachments/assets/6488a0b3-2621-4a63-826a-4136d4b3edbf" />

## ⭐ Conclusion

The Personal Expense Tracker is a simple and effective Python project that demonstrates the use of basic programming concepts such as functions, lists, dictionaries, modular coding, and JSON file handling.
It fulfills the requirement of solving a real-world problem by helping users record, organize, and understand their daily expenses.
All functionalities—adding expenses, viewing them, filtering, and calculating totals—work smoothly and provide a complete learning experience for beginners in Python.

