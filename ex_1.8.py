import numpy as np

# Create 2d array shape (3, 4) with random floats 1-100
# Find min and max value
# Round to nearest int

array_2d = np.random.uniform(1, 100, size=(3, 4))

max_value = np.max(array_2d)
min_value = np.min(array_2d)

rounded_array = np.round(array_2d)

print(f"Maximum value before rounding was {max_value} and minimum {min_value}")
print("\nThis is the array rounded\n")
print(rounded_array)