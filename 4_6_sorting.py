# In this script, we go through lesson 4.6 of Python NumPy for your
# Grandma course: Sorting. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-sorting/

# %% Import libraries

import numpy as np
# %% Sorting:
# sort gives a sorted copy of an array:
# sort(a, axis=-1, kind=None) where:
# 1) THe first argument is an array
# 2) axis: axis to sort along
# 3) kind: method to sort. By default, quickshort is used.
# Let's see some examples:
foo = np.array([1, 7, 3, 9, 0, 9, 1])
np.sort(foo)
# Notice that foo remains unchanged:
print(foo)
# nan's are sent to the end:
bar = np.array([5, np.nan, 3, 11])
np.sort(bar)
# Notice that by default the ordering is ascending.
# There isn't a straightforward method to order in descending order. There are
# two tricks to do it:
# 1) Sort in ascending order and reverse the output.
# 2) Negate an array, sort in ascending order, and negate the output.
# There are two differences between both ways. The first one sends nan's to the
# front of the output. The second one won't work on strings.
# Let's see some examples.
# Sort bar with the first method:
np.sort(bar)[::-1]
# and the second method:
-np.sort(-bar)
# The kind of shorting, quickshort, is unstable in the sense that identical
# values are randomly ordered. To get a stable ordering, set kind='stable':
np.sort(np.array([2, 1, 3, 2]))
np.sort(np.array([2, 1, 3, 2]), kind='stable')
# Both output look equal, but in the second one the order of the 2's is always
# the same, whereas it's unclear in first example.
# Let's work now with multidimensional arrays. We can choose the axis to sort:
boo = np.array([[10, 55, 12],
               [0, 81, 33],
               [92, 11, 3]])
# Sort each column independently
np.sort(a=boo, axis=0)
# Sort each row independently
np.sort(a=boo, axis=1)
# Sort last axis
np.sort(a=boo, axis=-1)
# What if we want to order according to the first element of each row? This
# would be equivalent to boo[[1, 0, 2]] in this particular example.
# This can be done with argsort(a, axis=-1, kind=None), which does not order the
# array, but it gives the set of indices giving the ordering.
# E.g.:
goo = np.array([3, 0, 10, 5])
np.argsort(goo)
goo[np.argsort(goo)]
# This is equivalent to np.sort(goo). Looking back to the previous example, we
# can sort according to the second column ascending:
boo[np.argsort(a=boo[:, 1])]
# to the last column descending:
boo[np.argsort(-boo[:, -1])]
