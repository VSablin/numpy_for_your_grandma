# In this script, we go through lesson 2.4 of Python NumPy for your
# Grandma course: Indexing And Modifying Multidimensional Arrays. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-indexing-and-modifying-multidimensional-arrays/

# %% Import libraries
import numpy as np

# %% Indexing and Modifying MultiD Arrays:
# Let's define a 3x4 array:
bar = np.array([[5, 10, 15, 20], [25, 30, 35, 40], [45, 50, 55, 60]])
# We can subset bar with two indices. E.g. element (1, 2):
bar[1, 2]
# The result is a number as a np.array.
# We can subset a row with one index. E.g. row 1:
bar[0]
# The result is a 1D np.array.
# If you want a row **as a** 1D array, use:
bar[0, None]
# or slicing
bar[:1]
# Negative indexing is also allowed:
bar[1:3, [-2, -1]]
# Modifying elements is fairly straightforward.
# An element:
bar[0, 0] = -1
# A row:
bar[1] = bar[2]
# Multiple elements:
bar[[0, 1, 2], [0, 1, 2]] = [0, 0, 0]
# For higher dimensional np arrays use np.array[axis 0 indices, axis 1 indices,
# axis 2 indices...]
