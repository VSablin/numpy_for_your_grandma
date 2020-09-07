# In this script, we go through lesson 2.1 of Python NumPy for your
# Grandma course: What's A NumPy Array. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-whats-a-numpy-array/

# %% Import libraries
import numpy as np

# %% Defining a 1D np array from a list:
arr = np.array([10, 20, 30, 40, 50])
# We can print it:
print(arr)
# check its dimensionality with .ndim:
arr.ndim
# and its shape with .shape:
arr.shape
# Notice that the output of .shape is a tuple. In this particular case of a 1D
# array, it is (n,), with n the number of elements.
# Finally, we can find the length:
len(arr)

# %% Defining a 2D np array from a list of lists:
arr_2d = np.array([[10, 20, 30, 40, 50],
                   [100, 200, 300, 400, 500]])
# We can print it:
print(arr_2d)
# check its dimensionality with .ndim:
arr_2d.ndim
# and its shape with .shape:
arr_2d.shape
# Now, the first element of the tuple is the number of lists and the second
# the number of elements in each list. If we understand arr_2d as a matrix and
# each list as a row, .shape gives (number of rows, number of columns).
# Finally, we can find the length:
len(arr_2d)
# This gives 2, since it finds the number of elements in the global list, which
# is 2: 2 lists.
# If you instead want the number of entries, you can use .size:
arr_2d.size
# You can find the kind of variable arr or arr_2d are with type():
type(arr_2d)
# You can also find the type of the elements of the array with .dtype:
arr_2d.dtype

# %% What makes a Np array?
# 1) Homogeneous data: All the elements in the np array must be the same type.
# 2) Rectangular structure: If an array contains some inner arrays
# (e.g. arr_2d), each sub-array must contain the same number of elements.
# Some examples:
np.array([1, 2, 3])  # 1D array of integers. Good praxis.
np.array([1, 'hello', 3])  # 1D array mixing integers and a string. The integers
# are coerced to strings. Bad praxis.
np.array([[1, 2, 3, 4], [5, 6, 5, 7]])  # 2D array of integers. Good praxis.
np.array([[1, 2, 3, 4], [5, 6]])  # Non-rectangular 2D array of integers. This
# is allowed. Each element of the array is a list.

# Remark: You can define higher dimensional np arrays. They follow the rules
# mentioned in the script.
