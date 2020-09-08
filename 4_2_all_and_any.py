# In this script, we go through lesson 4.3 of Python NumPy for your
# Grandma course: all and any. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-all-and-any/

# %% Import libraries

import numpy as np
# %% all() and any()
# all() identifies arrays where all the elements have some value and any arrays
# where some elements have some value. Let's see some examples:
foo = np.array([[np.nan, 4.4],
               [1.0, 3.2],
               [np.nan, np.nan],
               [0.1, np.nan]])
# Let's check which rows contain nan's:
mask = np.any(np.isnan(foo), axis=1)
print(mask)
# And we can use this to subset foo:
foo[mask]
# Another example:
mask = np.all(np.isnan(foo), axis=1)
print(mask)
foo[mask]
