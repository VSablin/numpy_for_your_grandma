# In this script, we go through lesson 2.3 of Python NumPy for your
# Grandma course: Indexing And Modifying 1D Arrays. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-indexing-and-modifying-1d-arrays/

# %% Import libraries
import numpy as np

# %% Indexing a 1D array:
foo = np.array([10, 20, 30, 40, 50])
# Access to ith element:
foo[0]
foo[1]
# Modify the ith element:
foo[1] = -20
# Access last element:
foo[len(foo) - 1]
# or negative indexing:
foo[-1]
# Access to several elements with lists:
foo[[0, 1, 4]]
foo[[2, 3, 2, 3]]
# or np.arrays with the indices:
foo[np.zeros(3, dtype='int64')]
# Slicing is allowed: np.array[start index:end index: jump by]
foo[:2]
foo[2:]
foo[::2]
# Modify multiple elements:
foo[[0, 1, 4]] = [100, 200, 400]
