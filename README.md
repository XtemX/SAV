# SAV
Small Python projects covering data structures and logic.

# Python Basic Projects 🐍

This repository contains a collection of Python scripts developed during my initial phase of learning programming. These projects focus on core concepts such as data structures, loops, and logic implementation.

## 🚀 Projects Overview

### 1. Inventory Management System (`inventory.py`)
A script that simulates a warehouse database using dictionaries and tuples.
* **Key Features:** Calculating total stock value with discounts, finding the most/least stocked items, and searching for specific products.
* **Concepts used:** Dictionaries, tuple unpacking, f-strings, and loops.

### 2. Flower Shop Logic (`flower_shop.py`)
A practical example of data analysis and decision-making based on user preferences.
* **Key Features:** Analyzing bouquet composition and determining customer satisfaction based on specific criteria.
* **Concepts used:** Dictionary methods (`.get()`, `.values()`), list comprehensions, and conditional logic.

### 3. Matrix Calculator (`matrix_math.py`)
A mathematical tool for processing multi-dimensional arrays.
* **Key Features:** Dynamic matrix creation from user input and calculating sums for each column.
* **Concepts used:** Nested loops, input validation (try-except), and multi-dimensional lists.

## 🛠️ Skills Demonstrated
* **Programming Language:** Python 3.x
* **Data Structures:** Lists, Dictionaries, Tuples
* **Logic:** Control flow, nested iterations, and error handling
* **Environment:** Developed using Visual Studio Code

---
*Developed by Artem Sochyvets as part of my journey toward becoming a Fachinformatiker für Anwendungsentwicklung.*

"""
Project: Inventory Management System
Description: Calculates total value of goods, finds most/least stocked items,
             and checks for specific products.
Author: Artem Sochyvets
"""

print("--- Inventory Report ---")

# Database of products
# ID: (Name, Price, Discount, Quantity, Shelf Life Days)
products = {
    101: ('Milk', 3.50, 0.50, 50, 7),
    102: ('Bread', 1.50, 0.20, 100, 3),
    103: ('Cheese', 12.0, 2.0, 30, 14),
    104: ('Yogurt', 2.50, 0.30, 60, 10),
    105: ('Sausage', 20.0, 3.0, 20, 10),
    106: ('Butter', 8.0, 1.0, 40, 20),
    107: ('Sugar', 1.80, 0.20, 70, 365),
    108: ('Oranges', 6.0, 1.0, 25, 14),
    109: ('Apples', 5.0, 0.8, 80, 20),
    110: ('Pasta', 4.0, 0.5, 60, 730)
}

# 1. Calculate Total Value
total_value = 0
for _, item in products.items():
    _, price, discount, quantity, _ = item  # Unpacking only needed values
    final_price = price - discount
    total_value += final_price * quantity

print(f"Total value of stock (after discounts): {total_value:.2f} EUR")

# 2. Find Most and Least Stocked Items
max_quantity = -1
min_quantity = float('inf')
most_stocked = []
least_stocked = []

for _, item in products.items():
    name, _, _, quantity, _ = item
    
    if quantity > max_quantity:
        max_quantity = quantity
        most_stocked = [name]
    elif quantity == max_quantity:
        most_stocked.append(name)
    
    if quantity < min_quantity:
        min_quantity = quantity
        least_stocked = [name]
    elif quantity == min_quantity:
        least_stocked.append(name)

print(f"Most stocked item(s) ({max_quantity} units): {', '.join(most_stocked)}")
print(f"Least stocked item(s) ({min_quantity} units): {', '.join(least_stocked)}")

# 3. Check for specific product (Oranges)
target_product = 'Oranges'
found = False
for _, item in products.items():
    name, price, discount, _, _ = item
    if name == target_product:
        final_price = price - discount
        print(f"✔️ {target_product} are in stock. Current price: {final_price:.2f} EUR")
        found = True
        break

if not found:
    print(f"❌ {target_product} are currently out of stock.")

print("------------------------")


******************************************************************************************************************************

"""
Project: Flower Shop Logic
Description: Analyzes bouquet composition and applies basic customer logic.
Author: Artem Sochyvets
"""

print("--- Bouquet Analysis ---")

# Defining the bouquet composition as a dictionary
# Flower Name: Quantity
bouquet = {
    "Rose": 15,
    "Daisy": 12,
    "Tulip": 8,
    "Lily": 5,
    "Chrysanthemum": 10,
    "Narcissus": 7,
    "Peony": 3,
    "Carnation": 9
}

# 1. Statistics
max_count = max(bouquet.values())
min_count = min(bouquet.values())
total_flowers = sum(bouquet.values())

# Find names of flowers with max/min quantity
flowers_most = [name for name, count in bouquet.items() if count == max_count]
flowers_least = [name for name, count in bouquet.items() if count == min_count]

print(f"Total flowers in bouquet: {total_flowers}")
print(f"Most abundant flower(s) ({max_count} units): {', '.join(flowers_most)}")
print(f"Least abundant flower(s) ({min_count} units): {', '.join(flowers_least)}")

# 2. Customer Logic Example
print("\n--- Customer Preference Check ---")
daisy_count = bouquet.get('Daisy', 0)

if daisy_count > 10:
    print(f"Result: The customer will like this bouquet (contains {daisy_count} Daisies).")
else:
    print(f"Result: The customer might not like this bouquet (less than 10 Daisies).")

print("-------------------------")

************************************************************************************************************************************************************

"""
Project: Matrix Mathematics
Description: Creates a matrix from user input and calculates column sums.
Author: Artem Sochyvets
"""

print("--- Matrix Calculator ---")

# 1. Input Dimensions
try:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
except ValueError:
    print("Error: Please enter integer numbers for dimensions.")
    exit()

# 2. Input Matrix Elements
matrix = []
print(f"\nPlease enter data for a {rows}x{cols} matrix:")

for r in range(rows):
    current_row = []
    for c in range(cols):
        while True:
            try:
                value = int(input(f"  Element [{r+1}][{c+1}] = "))
                current_row.append(value)
                break
            except ValueError:
                print("  Invalid input. Please enter an integer.")
    matrix.append(current_row)

# 3. Output and Calculation
print("\n--- Results ---")
print("Generated Matrix:")
for row in matrix:
    # Beautiful alignment using string formatting
    print("  " + "  ".join(f"{item:4}" for item in row))

print("\nColumn Sums:")
# Summing columns
for c in range(cols):
    col_sum = 0
    for r in range(rows):
        col_sum += matrix[r][c]
    print(f"  Sum of column {c+1}: {col_sum}")

print("-------------------------")




