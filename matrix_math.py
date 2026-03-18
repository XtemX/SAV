"""
Project: Matrix Mathematics
Description: Creates a matrix from user input and calculates column sums.
"""

print("--- Matrix Calculator ---")

try:
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))
    
    matrix = []
    for r in range(rows):
        row_data = []
        for c in range(cols):
            val = int(input(f"  Element [{r+1}][{c+1}]: "))
            row_data.append(val)
        matrix.append(row_data)

    print("\nGenerated Matrix:")
    for row in matrix:
        print("  " + "  ".join(f"{item:4}" for item in row))

    print("\nColumn Sums:")
    for c in range(cols):
        c_sum = sum(matrix[r][c] for r in range(rows))
        print(f"  Column {c+1}: {c_sum}")

except ValueError:
    print("Error: Please enter valid integers.")
