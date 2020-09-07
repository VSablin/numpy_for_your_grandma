# In this script, we go through lesson 3.4 of Python NumPy for your
# Grandma course: Boolean Indexing. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-boolean-indexing/

# %% Import libraries

import numpy as np
# %% Boolean Indexing:
# Booleans can be used to subset arrays. For instance, given this array:
foo = np.array([[3, 9, 7], [2, 0, 3], [3, 3, 1]])
# imagine you want to replace all the 3's by 0's. We can do this by defining
# a boolean array with the desired condition:
mask = (foo == 3)
# Now we can subset:
foo[mask]
# and replace:
foo[mask] = 0
print(foo)
# We can also subset rows and columns with booleans:
rows_1_and_3 = np.array([True, False, True])
cols_2_and_3 = np.array([False, True, True])
foo[rows_1_and_3]
foo[:, cols_2_and_3]
# The combination of both is not that intuitive:
foo[rows_1_and_3, cols_2_and_3]
# np understands this as:
foo[[0, 2], [1, 2]]
# In other words, foo[rows_1_and_3] is equivalent to foo[[0,2]] and
# foo[cols_2_and_3] is foo[:,[1,2]]
# We can do boolean operations:
# 1) AND: &
# 2) OR: |
# 3) XOR: ^
# 4) NOT: ~
# We can apply this to indexing. Let us see some examples:
names = np.array(['Dennis', 'Dee', 'Charlie', 'Mac', 'Frank'])
ages = np.array([43, 44, 44, 42, 74])
genders = np.array(['male', 'female', 'male', 'male', 'male'])
# As an easy example, we can find who are 44 or older:
names[ages >= 44]
# But we can combine conditions; e.g., which males are older than 42:
names[(genders == 'male') & (ages > 42)]
# Remember to put all the logical conditions in parenthesis.
# Who's not a male or is younger than 43:
names[~(genders == 'male') | (ages < 43)]
