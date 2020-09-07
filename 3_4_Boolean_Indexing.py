# In this script, we go through lesson 3.4 of Python NumPy for your
# Grandma course: Boolean Indexing. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-boolean-indexing/

# %% Import libraries

import numpy as np
# %% Boolean Indexing:
# Booleans can be used to subset arrays. For instance, given this array:
foo = np.array([[3, 9, 7], [2, 0, 3], [3, 3, 1]])
# imagine you want to replace all the 3's by 0's.
