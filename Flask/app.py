from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def read_expenses():
    expenses = []
    with open('expenses.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert amount to a float for calculation purposes
            row['amount'] = float(row['amount'])
            expenses.append(row)
    return expenses

@app.route('/')
def index():
    # Get filter parameter from the query string (if any)
    category_filter = request.args.get('category', '').strip()
    all_expenses = read_expenses()
    
    # Filter expenses by category if a filter is provided
    if category_filter:
        expenses = [exp for exp in all_expenses if exp['category'].lower() == category_filter.lower()]
    else:
        expenses = all_expenses

    # Calculate total spending on the displayed expenses
    total = sum(expense['amount'] for expense in expenses)

    # Get a sorted list of unique categories for the filter dropdown
    unique_categories = sorted({exp['category'] for exp in all_expenses})
    
    return render_template(
        'index.html',
        expenses=expenses,
        total=total,
        category_filter=category_filter,
        unique_categories=unique_categories
    )

if __name__ == '__main__':
    app.run(debug=True)
