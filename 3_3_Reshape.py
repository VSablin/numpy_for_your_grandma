# In this script, we go through lesson 3.3 of Python NumPy for your
# Grandma course: Reshape. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-reshape/

# %% Import libraries

import numpy as np
# %% Reshape
# Reshaping is typically needed. It can be done with .reshape() method or
# np.reshape() function.
# E.g., we can convert a 1D array to a 2D in both ways:
foo = np.arange(start=1, stop=9)
bar = foo.reshape((2, 4))
bar = np.reshape(a=foo, newshape=(2, 4))
# We can also reshape bar as a (4, 2) array:
bar.reshape((4, 2), order='C')
# order='C' implies that the last axis is reordered first. It is the default
# option. It is C-style (C, the language!). Alternatively:
bar.reshape((4, 2), order='F')
# order='F' implies that the first axis is reordered firt. 'F' stands for
# Fortran here :)
# Transposing matrices is also possible with .T or np.transpose():
bar.T
np.transpose(bar)
# It is also possible to reshape to higher dimensional arrays:
bar.reshape((2, 2, 2))
# If you want to reshape something to (d1, dn), being dn the last dimension of
# the array to be reshaped and d1 the product of the rest, negative indexing
# is possible (even the meaning has nothing to do with negative indexing for
# subsetting).
bar.reshape((-1, 2))
# Finally, the product of the elements of the tuple must be equal to the number
# of elements of the array. Otherwise, you get an error:
bar.reshape((2, 2, 3))
