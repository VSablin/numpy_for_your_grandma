# In this script, we go through lesson 3.2 of Python NumPy for your
# Grandma course: Newaxis. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-newaxis/

# %% Import libraries

import numpy as np
# %% Newaxis
# Sometimes, you may want to modify the dimensionality of an array to do some
# operations. For instance, you may want to add a new axis. This is done with
# newaxis.
# E.g., imagine you have these arrays:
A = np.array([3, 11, 4, 5])
B = np.array([5, 0, 3])
# These are not compatible ((4,) and (3,)). But maybe we want to make operations
# as if they were (4, 1) and (1, 3). This can be done with np.newaxis:
B[:, np.newaxis]
A[np.newaxis, :]
# np.newaxis is equivalent to None:
B[:, None]
A[None, :]
# Let's see that it works!
A[None, :] - B[:, None]
