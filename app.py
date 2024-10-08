from flask import Flask, render_template, request, redirect, url_for, make_response
from datetime import datetime
import csv
from io import StringIO

app = Flask(__name__)

# Dictionary to store expenditures grouped by date
expenditures_dict = {}

# Sample inventory for the store
inventory = [
    {'name': 'Apple', 'price': 0.5, 'quantity': 100},
    {'name': 'Banana', 'price': 0.3, 'quantity': 150},
    {'name': 'Orange', 'price': 0.6, 'quantity': 80},
    {'name': 'Grapes', 'price': 2.0, 'quantity': 50},
    {'name': 'Mango', 'price': 1.5, 'quantity': 60},
]

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for inventory management with search functionality
@app.route('/inventory', methods=['GET', 'POST'])
def inventory_management():
    global inventory

    # Handle search query
    query = request.args.get('search')  # Get the search query from the search form

    # Filter the inventory based on the search query
    if query:
        filtered_inventory = [item for item in inventory if query.lower() in item['name'].lower()]
    else:
        filtered_inventory = inventory

    if request.method == 'POST':
        item_name = request.form.get('item_name')
        item_price = request.form.get('item_price')
        item_quantity = request.form.get('item_quantity')

        # Add new item to inventory
        inventory.append({
            'name': item_name,
            'price': float(item_price),
            'quantity': int(item_quantity)
        })

        return redirect(url_for('inventory_management'))

    return render_template('inventory.html', inventory=filtered_inventory)

# Route to sell an item
@app.route('/sell', methods=['POST'])
def sell_item():
    item_name = request.form.get('item_name')
    item_quantity_sold = int(request.form.get('item_quantity_sold'))
    current_date = datetime.now().strftime("%Y-%m-%d")
    time_added = datetime.now().strftime("%H:%M:%S")

    for item in inventory:
        if item['name'] == item_name and item['quantity'] >= item_quantity_sold:
            # Update inventory quantity
            item['quantity'] -= item_quantity_sold

            # Update expenditures
            if current_date not in expenditures_dict:
                expenditures_dict[current_date] = {'items': [], 'total': 0}

            # Add the sold item to the expenditures dictionary
            expenditures_dict[current_date]['items'].append({
                'name': item_name,
                'price': item['price'],
                'quantity': item_quantity_sold,
                'time': time_added
            })
            expenditures_dict[current_date]['total'] += item['price'] * item_quantity_sold

            break

    return redirect(url_for('expenditures'))

# Route for expenditure tracking
@app.route('/expenditures', methods=['GET', 'POST'])
def expenditures():
    current_date = datetime.now().strftime("%Y-%m-%d")
    selected_date = request.args.get('date', current_date)  # Get the date from the query parameters

    if request.method == 'POST':
        # Handle adding a new expenditure
        item_name = request.form.get('item_name')
        item_price = request.form.get('item_price')
        item_quantity = request.form.get('item_quantity')

        # Get the current time
        time_added = datetime.now().strftime("%H:%M:%S")

        # Append new item to the expenditures dictionary for the selected date
        if selected_date not in expenditures_dict:
            expenditures_dict[selected_date] = {'items': [], 'total': 0}

        # Add the item
        expenditures_dict[selected_date]['items'].append({
            'name': item_name,
            'price': float(item_price),
            'quantity': int(item_quantity),
            'time': time_added
        })

        # Update the total amount for the day
        expenditures_dict[selected_date]['total'] += float(item_price) * int(item_quantity)

        return redirect(url_for('expenditures', date=selected_date))

    # Render the expenditures for the selected date
    return render_template('expenditures.html', expenditures=expenditures_dict.get(selected_date, {'items': [], 'total': 0}), current_date=current_date, selected_date=selected_date)

# Route to remove an expenditure
@app.route('/remove_expenditure', methods=['POST'])
def remove_expenditure():
    selected_date = request.form.get('date')
    item_name = request.form.get('item_name')

    if selected_date in expenditures_dict:
        expenditures_dict[selected_date]['items'] = [
            item for item in expenditures_dict[selected_date]['items'] if item['name'] != item_name
        ]
        expenditures_dict[selected_date]['total'] = sum(item['price'] * item['quantity'] for item in expenditures_dict[selected_date]['items'])

    return redirect(url_for('expenditures', date=selected_date))

# Route to export expenditures to CSV
@app.route('/export_expenditures', methods=['GET'])
def export_expenditures():
    si = StringIO()
    writer = csv.writer(si)

    # Write CSV headers
    writer.writerow(['Date', 'Item Name', 'Price', 'Quantity', 'Time'])

    # Write each expenditure entry
    for date, data in expenditures_dict.items():
        for item in data['items']:
            writer.writerow([date, item['name'], item['price'], item['quantity'], item['time']])

    # Create the CSV response
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=expenditures.csv"
    output.headers["Content-type"] = "text/csv"

    return output

# Route for the online shop
@app.route('/shop')
def shop():
    return render_template('shop.html')

# Route for the change calculator
@app.route('/change_calculator', methods=['GET', 'POST'])
def change_calculator():
    change = None
    total_cost = None
    amount_paid = None

    if request.method == 'POST':
        total_cost = float(request.form.get('total_cost'))
        amount_paid = float(request.form.get('amount_paid'))
        change = amount_paid - total_cost  # Calculate change

    return render_template('change_calculator.html', change=change, total_cost=total_cost, amount_paid=amount_paid)

if __name__ == '__main__':
    app.run(debug=True)
