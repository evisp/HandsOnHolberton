import csv
from datetime import datetime

CSV_FILE = 'expenses.csv'
FIELDNAMES = ['date', 'category', 'amount', 'description']

def read_expenses():
    """Reads expenses from the CSV file and returns a list of dictionaries."""
    expenses = []
    try:
        with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert the amount to float
                row['amount'] = float(row['amount'])
                # Parse the date string into a datetime object for filtering/sorting
                try:
                    row['date_obj'] = datetime.strptime(row['date'], '%Y-%m-%d')
                except ValueError:
                    row['date_obj'] = None
                expenses.append(row)
    except FileNotFoundError:
        # If the CSV doesn't exist, return an empty list
        pass
    return expenses

def append_expense(expense):
    """Appends a new expense (a dict with keys matching FIELDNAMES) to the CSV file."""
    file_exists = False
    try:
        # Check if the file exists by attempting to open it in read mode.
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as csvfile:
            file_exists = True
    except FileNotFoundError:
        file_exists = False
    
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        if not file_exists:
            # If the file didn't exist, write the header first.
            writer.writeheader()
        writer.writerow(expense)
