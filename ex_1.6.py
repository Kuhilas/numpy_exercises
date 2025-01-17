import numpy as np

# Generate 2d array with shape (4,5) rand ints between 10-50
# Calculate the median of the array

array_2d = np.random.randint(10, 51, size=(4, 5))

array_2d_median = np.median(array_2d)
print(array_2d_median)