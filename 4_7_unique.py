# In this script, we go through lesson 4.7 of Python NumPy for your
# Grandma course: unique. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-unique/

# %% Import libraries

import numpy as np
# %% unique:
# Extract the unique elements of an array. E.g.:
gar = np.array(['b', 'b', 'a', 'a', 'c', 'c'])
np.unique(gar)
# Notice that they are sorted in ascending order. Passing the argument
# return_index=True, we get a tuple with the indices where each element
# appears for the first time in the original array.
np.unique(gar, return_index=True)
# This can be combined with argsort to get uniques in the order in which
# they appear in the original array:
uniques, first_indices = np.unique(gar, return_index=True)
uniques[np.argsort(first_indices)]
# Another handy argument of unique is return_counts:
np.unique(gar, return_counts=True)
# It gives the number of times each element appears as a second output (third
# if you also set return_index=True).
