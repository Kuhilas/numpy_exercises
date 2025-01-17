import numpy as np

# Generate an array of 25 rand ints between -100 and 100 using numpy.random
# calculate the mean

random_int_array = np.random.randint(-100, 101, size=25)
random_array_mean = np.mean(random_int_array)

print(random_array_mean)