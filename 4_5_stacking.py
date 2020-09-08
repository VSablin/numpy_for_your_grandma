# In this script, we go through lesson 4.5 of Python NumPy for your
# Grandma course: Stacking. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-stacking/

# %% Import libraries

import numpy as np
# %% Stacking:
# Functions hstack(), vstack(), and stack() are similar to concatenate().
# vstack is equivalent to concatenate in the first axis after 1-D arrays of
# shape (N,) are reshaped to (1, N).
# hstack is equivalent to concatenate in the second axis, except for 1-D arrays,
# where it concatenates along the first axis.
# stack concatenates along a newly specified axis.
# Let's see all of them in more details.
# The argument of vstack is a sequence of arrays as a tuple. It does the
# following:
# 1) Each array in the sequence, if it is 1d, is promoted to 2D giving a new
# front axis.
# 2) If, after 1), all the arrays have the same dimensionality, concatenate
# along axis 0.
# 3) If the conditions of 2) are not fulfilled, throw an error.
# Let's see some examples:
foo = np.array(['a', 'b'])
bar = np.array(['c', 'd'])
baz = np.array([['e', 'f']])
bingo = np.array([['g', 'h', 'i']])
# We can vstack foo and bar:
np.vstack((foo, bar))
# We can vstack foo, bar, and baz:
np.vstack((foo, bar, baz))
# But we cannot vstack baz and bingo:
np.vstack((baz, bingo))
# The argument of hstack is a sequence of arrays as a tuple. It does the
# following:
# 1) If every array in the sequence is 1D, concatenate arrays along axis 0.
# 2) else, if every array has the same shape excluding axis 1, concatenate
# along axis 1.
# 3) Otherwise, throw an error.
# Let's see some examples:
foo = np.array(['a', 'b'])
bar = np.array(['c', 'd'])
baz = np.array([['e', 'f']])
bingo = np.array([['g', 'h', 'i']])
bongo = np.array([['j', 'k'],
                 ['l', 'm']])
# We can hstack foo and bar:
np.hstack((foo, bar))
# We can hstack baz and bingo:
np.hstack((baz, bingo))
# But we cannot hstack foo and bingo:
np.hstack((foo, bingo))
# We cannot hstack bingo and bongo:
np.hstack((bingo, bongo))
# The first argument of stack is a sequence of arrays as a tuple. The second is
# axis, the new axis to insert and combine the arrays along. It does the
# following:
# 1) If every array in the sequence is 1D, concatenate arrays along axis 0.
# 2) else, if every array has the same shape excluding axis 1, concatenate
# along axis 1.
# 3) Otherwise, throw an error.
# Let's see some examples:
foo = np.array(['a', 'b'])
bar = np.array(['c', 'd'])
baz = np.array([['e', 'f']])
bingo = np.array([['g', 'h', 'i']])
bongo = np.array([['j', 'k'],
                 ['l', 'm']])
# We can hstack foo and bar:
np.hstack((foo, bar))
# We can hstack baz and bingo:
np.hstack((baz, bingo))
# But we cannot hstack foo and bingo:
np.hstack((foo, bingo))
# We cannot hstack bingo and bongo:
np.hstack((bingo, bongo))
