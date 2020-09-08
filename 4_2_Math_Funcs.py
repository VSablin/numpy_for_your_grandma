# In this script, we go through lesson 4.2 of Python NumPy for your
# Grandma course: Math Funcs. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-math-funcs/

# %% Import libraries

import numpy as np
# %% Math Funcs:
# np provides a lot of mathematical functions, such as sum, mean, min, max,
# floor, round, exp, log... ALl of them have similar interfaces and behaviour.
# Let's define a 2D np array and see some examples:
squee = np.array([[5.0, 2.0, 9.0],
                 [1.0, 0.0, 2.0],
                 [1.0, 7.0, 8.0]])
# Summing all the elements of the array:
np.sum(squee)
# Column sum:
np.sum(squee, axis=0)
# Row sum:
np.sum(squee, axis=1)
# In the last two examples, np gives a 1D array as an output. To keep the
# original dimensionality, we can use keepdims=True:
np.sum(squee, axis=0, keepdims=True)
# nan values:
squee[0, 0] = np.nan
np.sum(squee)
# The result is nan. nan's can be ignored with where argument:
np.sum(squee, where=~np.isnan(squee))
# Alternatively:
np.nansum(squee)
# This function treats all nan's as 0's.
