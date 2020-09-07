# In this script, we go through lesson 3.1 of Python NumPy for your
# Grandma course: Broadcasting. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-broadcasting/

# %% Import libraries

import numpy as np
# %% Broadcasting
# np has broadcasting tools to combine np arrays with different dimensions.
# Image we have a 4x3 array:
bart = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
# and we want to add 5 to the first column, 3 to the second, and 10
# to the third. We can do this by defining:
lisa = np.array([[5, 3, 10], [5, 3, 10], [5, 3, 10], [5, 3, 10]])
bart + lisa
# However, np allows to do this much easily:
lisa = np.array([[5, 3, 10]])
bart + lisa
# or even
lisa = np.array([5, 3, 10])
bart + lisa
# This is called broadcasting.
# More simple examples:
np.array([1, 2, 3]) + 0.5
np.array([1, 2, 3]) * -1
# In some cases there is no possible broadcating:
bart + np.array([0, 0, 0, 0])
# The general rules of broadcating are the following:
# 1) Suppose we want to operate (sum, rest, etc.) with two arrays A and B.
# 2) np moves backwards from the last dimension of each array to check whether
# they are compatible. Dimensions are compatible if they are equal or either of
# them is 1.
# 3) If all the dimensions are compatible, A and B are compatible arrays.
# For instance:
np.random.seed(1234)
A = np.random.randint(low=1, high=10, size=(3, 4))
B = np.random.randint(low=1, high=10, size=(3, 1))
# Ths shapes are (3, 4) and (3, 1). Going backwards from the last dimension, we
# see that the 2nd dimension is compatible (4 and 1). Then, np conceptually
# spans the second dimension to 4 by making 4 identical copies. The first dim
# is also compatoble , so A and B are compatible.
# Another example:
np.random.seed(4321)
A = np.random.randint(low=1, high=10, size=(4, 4))
B = np.random.randint(low=1, high=10, size=(2, 1))
# The second dimension is compatible. np, effectively, would make 4 copies of B
# in the second axis. However, the first dimension is not compatible, so A and
# B are not compatible.
# One more:
np.random.seed(1111)
A = np.random.randint(low=1, high=10, size=(3, 1, 4))
B = np.random.randint(low=1, high=10, size=(2, 1))
# First compare the last dimension of both arrays: 4 for A and 1 for B, so they
# are compatible and np makes 4 copies of B in this axis. Now, np compares the
# next one: 1 for A and 2 for B. They are again compatible and np makes 2 copies
# of A in that dimension. Finally, we are left with 3 for A and no dimension for
# B. In this case, np assigns a dimension of 1 for this axis in B, so they are
# compatible arrays.
