# Define the input sequence u[k] for k = 0 to 8
u = [1, 2, 0, 3, 1, 2, 1, 0, 0]  # u[0] to u[8]

# Initialize y[k] for each part (a) to (d) with zeros
y_a = [0] * 9
y_b = [0] * 9
y_c = [0] * 9
y_d = [0] * 9

# Compute y[k] for each difference equation
for k in range(9):
    # Part a) y[k] = -y[k-1] + u[k-1]
    if k >= 1:
        y_a[k] = -y_a[k-1] + u[k-1]
    else:
        y_a[k] = 0  # y[k] = 0 for k <= 0
    
    # Part b) y[k] = u[k-1] + u[k-2] + u[k-3]
    y_b[k] = 0
    for n in range(1, 4):
        if k - n >= 0:
            y_b[k] += u[k - n]
        # If k - n < 0, u[k - n] is considered 0
    
    # Part c) y[k] = 0.5u[k-1] + 0.5u[k-2]
    y_c[k] = 0
    if k >= 1:
        y_c[k] += 0.5 * u[k - 1]
    if k >= 2:
        y_c[k] += 0.5 * u[k - 2]
    
    # Part d) y[k] = y[k-1] + y[k-2] + u[k-1]
    if k >= 1:
        y_d[k] += y_d[k-1] + u[k-1]
    if k >= 2:
        y_d[k] += y_d[k-2]
    # For k <1, y[k] remains 0

# Display the results
print("\nDifference Equations Results:")
print("-" * 50)
print(f"{'k':^5}{'y_a[k]':^12}{'y_b[k]':^12}{'y_c[k]':^12}{'y_d[k]':^12}")
print("-" * 50)
for k in range(9):
    print(f"{k:^5}{y_a[k]:^12.2f}{y_b[k]:^12.2f}{y_c[k]:^12.2f}{y_d[k]:^12.2f}")
print("-" * 50)