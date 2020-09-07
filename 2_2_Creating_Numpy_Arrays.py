# In this script, we go through lesson 2.2 of Python NumPy for your
# Grandma course: Creating Numpy Arrays. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-creating-numpy-arrays/

# %% Import libraries
import numpy as np

# %% Creating np arrays from scratch:
# There are many ways to do it.
# 1) You can make a 1D array from a list:
np.array(['a', 'b', 'c'])
# 2) You can make a 2D array from a list of lists:
np.array([['a', 'b'], ['c', 'd'], ['e', 'f']])
# 3) You can make an array of 0s with np.zeros():
np.zeros(shape=(3, 5))
# 4) You can use np.full() to initialise an array full of a particular value:
np.full(shape=(3, 5), fill_value='cat')
# 5) You can make a sequence with np.arange():
np.arange(start=1, stop=5, step=1)
# Remark: start is included in the array, but stop is not.
# 6) You can use np.random.randint() to make an array of random integers:
np.random.randint(low=1, high=7, size=(2, 3))
