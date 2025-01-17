import numpy as np

# Round and median of 1d floats

arr_1d = np.array([1.45406577, 8.27393835, 9.86579627, 4.59713858,
 9.58083817, 2.57662887, 3.44091756, 5.41150921, 6.72276201, 
 6.58891703, 7.77308988, 1.26170442, 8.15367039, 4.43046578, 3.16993445])


arr_median = np.median(arr_1d)
arr_rounded = np.round(arr_1d)

print(arr_median)
print(arr_rounded)