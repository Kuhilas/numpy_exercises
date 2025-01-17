import numpy as np

# Create 1d array with 10 random floats from -5 and 5. 
# Calculate the mean and round each float to 2 decimal pieces

random_float_array = np.random.uniform(-5, 5, size=10)

rounded_array = np.round(random_float_array, decimals=2)

print(rounded_array)

rounder_array_mean = np.mean(rounded_array)

print(rounder_array_mean)