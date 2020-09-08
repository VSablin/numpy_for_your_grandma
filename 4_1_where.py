# In this script, we go through lesson 4.1 of Python NumPy for your
# Grandma course: where. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-where/

# %% Import libraries

import numpy as np
# %% where:
# Suppose you have two 1D arrays with the same length, foo and bar, and you want
# to define a third one baz such that, if the i-th element of bar is 0, the i-th
# element of baz is twice the i-th element of foo, and otherwise you take half
# the corresponding value of foo. Let's define foo and bar:
foo = np.array([1, 2, 3, 4, 5])
bar = np.array([0, 1, 0, 0, 1])
# This can be done with a for loop:
baz = np.zeros(foo.shape[0])
for i in range(foo.shape[0]):
    if bar[i] == 0:
        baz[i] = 2 * foo[i]
    else:
        baz[i] = foo[i] / 2
# But this for loop will be extremely slow for large arrays, since np is calling
# all the time to C functions and this communication takes time. Alternatively,
# we can use boolean conditions:
baz = np.zeros(foo.shape[0])
baz[bar == 0] = 2 * foo[bar == 0]
baz[~(bar == 0)] = foo[~(bar == 0)] / 2
print(baz)
# There is shortcut of this operations using where(condition, x, y), being
# condition a boolean array, x the values to use when condition is True and y
# values otherwise:
baz = np.zeros(foo.shape[0])
baz = np.where((bar == 0),
               foo * 2,
               foo / 2)
