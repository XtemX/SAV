"""
Project: Flower Shop Logic
Description: Analyzes bouquet composition and applies basic customer logic.
"""

print("--- Bouquet Analysis ---")

bouquet = {
    "Rose": 15, "Daisy": 12, "Tulip": 8, "Lily": 5,
    "Chrysanthemum": 10, "Narcissus": 7, "Peony": 3, "Carnation": 9
}

# Statistics
total = sum(bouquet.values())
max_f = max(bouquet.values())
most_popular = [name for name, count in bouquet.items() if count == max_f]

print(f"Total flowers: {total}")
print(f"Main flower(s): {', '.join(most_popular)} ({max_f} units)")

# Customer Logic
daisies = bouquet.get('Daisy', 0)
if daisies > 10:
    print(f"Result: Customer is happy! (Contains {daisies} Daisies)")
else:
    print("Result: Customer might be disappointed (not enough Daisies).")
