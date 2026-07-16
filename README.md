# Personal Finance Tracker

## Video demo:

https://youtu.be/ftJ5ahvdnSw

---

## Overview

Personal Finance Tracker is a command-line application developed in Python that helps users manage their personal finances efficiently. It allows users to record income and expenses, edit or delete transactions, search financial records, generate monthly reports, monitor spending statistics, and manage a monthly budget.

The project is designed to provide a simple and organized way to keep track of financial activities while demonstrating core Python programming concepts such as functions, dictionaries, lists, file handling with JSON, exception handling, modular programming, and testing with pytest.

This project was developed as the final project for **Harvard's CS50P: Introduction to Programming with Python**.

---

## Features

- Add income transactions
- Add expense transactions
- View all transactions
- Edit existing transactions
- Delete transactions
- Search transactions by:
  - Type
  - Category
  - Description
  - Date
- Generate monthly financial reports
- View financial statistics
- Set and manage a monthly budget
- Automatically save data using JSON
- Automatically load saved data when the program starts

---

## Technologies Used

- Python 3
- JSON
- Pytest

---

## Project Structure

```
Personal Finance Tracker/
│
├── main.py              # Main menu and program execution
├── finance.py           # Transaction and budget management
├── reports.py           # Monthly reports and statistics
├── storage.py           # Load and save data using JSON
├── data.json            # Stores transactions and budget
├── .gitignore
└── tests/
    └── test_project.py
```

---

## How to Run

1. Clone the repository:

```bash
git clone <https://github.com/mubashiraaqeel/Personal-Finance-Tracker>
```

2. Navigate to the project folder:

```bash
cd Personal-Finance-Tracker
```

3. Run the program:

```bash
python main.py
```

---

## Data Storage

The application stores all financial records in a `data.json` file.

The following information is saved automatically:

- Monthly budget
- Income transactions
- Expense transactions

When the application starts, previously saved data is automatically loaded.

---

## Testing

The project includes automated tests written using **pytest**.

To run the tests:

```bash
pytest
```

---

## Concepts Demonstrated

This project demonstrates the use of:

- Functions
- Loops
- Conditional statements
- Dictionaries
- Lists
- Exception handling
- File handling
- JSON serialization
- Modular programming
- Pytest unit testing

---

## Future Improvements

Possible future enhancements include:

- User authentication
- Password protection
- Graphical reports and charts
- CSV and Excel export
- Database integration using SQLite
- Web application using Flask

---

## Author

**Mubashira Aqeel**

BS Data Science Student

University of Engineering and Technology (UET)

Harvard CS50P Final Project
