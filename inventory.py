"""
Project: Inventory Management System
Description: Calculates total value of goods, finds most/least stocked items, 
             and checks for specific products.
"""

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

print("--- Inventory Report ---")

# 1. Calculate Total Value after discounts
total_value = 0
for _, item in products.items():
    _, price, discount, quantity, _ = item
    total_value += (price - discount) * quantity

print(f"Total value of stock: {total_value:.2f} EUR")

# 2. Find Most and Least Stocked Items
max_q = max(item[3] for item in products.values())
min_q = min(item[3] for item in products.values())

most_stocked = [item[0] for item in products.values() if item[3] == max_q]
least_stocked = [item[0] for item in products.values() if item[3] == min_q]

print(f"Most stocked: {', '.join(most_stocked)} ({max_q} units)")
print(f"Least stocked: {', '.join(least_stocked)} ({min_q} units)")

# 3. Search Example
target = 'Oranges'
found = any(item[0] == target for item in products.values())
print(f"Status for '{target}': {'In Stock' if found else 'Out of Stock'}")
