from flask import Flask, render_template, request, redirect, url_for, send_file
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

def read_expenses():
    expenses = []
    try:
        with open('expenses.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert amount to float
                row['amount'] = float(row['amount'])
                # Parse date into a datetime object for filtering/sorting
                try:
                    row['date_obj'] = datetime.strptime(row['date'], '%Y-%m-%d')
                except ValueError:
                    row['date_obj'] = None
                expenses.append(row)
    except FileNotFoundError:
        # If file doesn't exist, return an empty list
        pass
    return expenses

@app.route('/')
def index():
    # Get filter parameters from query string
    category_filter = request.args.get('category', '').strip()
    start_date_str = request.args.get('start_date', '').strip()
    end_date_str = request.args.get('end_date', '').strip()
    sort_by = request.args.get('sort_by', '').strip()

    all_expenses = read_expenses()

    # Apply category filter if specified
    filtered_expenses = all_expenses
    if category_filter:
        filtered_expenses = [exp for exp in filtered_expenses if exp['category'].lower() == category_filter.lower()]

    # Apply date range filters if provided
    if start_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            filtered_expenses = [exp for exp in filtered_expenses if exp['date_obj'] and exp['date_obj'] >= start_date]
        except ValueError:
            pass
    if end_date_str:
        try:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            filtered_expenses = [exp for exp in filtered_expenses if exp['date_obj'] and exp['date_obj'] <= end_date]
        except ValueError:
            pass

    # Sorting options
    if sort_by:
        if sort_by == 'date':
            filtered_expenses.sort(key=lambda x: x['date_obj'] if x['date_obj'] else datetime.min)
        elif sort_by == 'amount':
            filtered_expenses.sort(key=lambda x: x['amount'])
        elif sort_by == 'category':
            filtered_expenses.sort(key=lambda x: x['category'])

    # Calculate total expense amount
    total = sum(exp['amount'] for exp in filtered_expenses)

    # Get a sorted list of unique categories for the filter dropdown
    unique_categories = sorted({exp['category'] for exp in all_expenses})
    
    return render_template('index.html',
                           expenses=filtered_expenses,
                           total=total,
                           category_filter=category_filter,
                           start_date=start_date_str,
                           end_date=end_date_str,
                           sort_by=sort_by,
                           unique_categories=unique_categories)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date_val = request.form.get('date', '').strip()
        category = request.form.get('category', '').strip()
        amount = request.form.get('amount', '').strip()
        description = request.form.get('description', '').strip()

        # Minimal validation: date, category, and amount are required
        if not (date_val and category and amount):
            return render_template('add_expense.html',
                                   error="Please fill in all required fields.",
                                   form=request.form)

        try:
            amount_val = float(amount)
        except ValueError:
            return render_template('add_expense.html',
                                   error="Amount must be a valid number.",
                                   form=request.form)

        # Append new expense to CSV
        with open('expenses.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Assume the CSV already exists with headers
            writer.writerow({
                'date': date_val,
                'category': category,
                'amount': amount_val,
                'description': description
            })

        return redirect(url_for('index'))

    return render_template('add_expense.html')

@app.route('/chart')
def chart():
    expenses = read_expenses()
    # Compute total spending per category
    category_totals = {}
    for exp in expenses:
        cat = exp['category']
        category_totals[cat] = category_totals.get(cat, 0) + exp['amount']

    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    # Create a pie chart using matplotlib
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

    # Save the plot to a bytes buffer and return as an image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()  # Clean up the figure

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
