from finance import transactions
from reports import calculate_balance, calculate_average


# -------------------------
# Tests for finance.py
# -------------------------

def test_add_income():
    transactions.clear()

    transactions.append({
        "Type": "Income",
        "Amount": 5000,
        "Category": "Salary",
        "Description": "Monthly salary",
        "Date": "2026-07-12"
    })

    assert len(transactions) == 1
    assert transactions[0]["Type"] == "Income"
    assert transactions[0]["Amount"] == 5000


def test_add_expense():
    transactions.clear()

    transactions.append({
        "Type": "Expense",
        "Amount": 2000,
        "Category": "Food",
        "Description": "Lunch",
        "Date": "2026-07-12"
    })

    assert len(transactions) == 1
    assert transactions[0]["Type"] == "Expense"
    assert transactions[0]["Amount"] == 2000


def test_delete_transaction():
    transactions.clear()

    transaction = {
        "Type": "Expense",
        "Amount": 1000,
        "Category": "Transport",
        "Description": "Bus fare",
        "Date": "2026-07-12"
    }

    transactions.append(transaction)

    transactions.remove(transaction)

    assert len(transactions) == 0


# -------------------------
# Tests for reports.py
# -------------------------

def test_calculate_balance_positive():
    assert calculate_balance(5000, 2000) == 3000


def test_calculate_balance_zero():
    assert calculate_balance(1000, 1000) == 0


def test_calculate_balance_negative():
    assert calculate_balance(1000, 2000) == -1000


def test_calculate_average():
    assert calculate_average(1000, 4) == 250


def test_calculate_average_zero_count():
    assert calculate_average(1000, 0) == 0