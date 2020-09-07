# In this script, we go through lesson 2.5 of Python NumPy for your
# Grandma course: Basic Math. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-basic-math/

# %% Import libraries
import numpy as np

# %% Basic Math
foo = np.array([[4, 3], [1, 0]])
bar = np.array([[1, 2], [3, 4]])
# Element-wise operations:
foo + bar
foo - bar
foo * bar
foo / bar
# Matrix multiplication:
foo @ bar
