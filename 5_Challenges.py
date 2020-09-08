# In this script, we go through lesson 5 of Python NumPy for your
# Grandma course: Challenges. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-challenges/

# %% Import libraries
import numpy as np

# %% Challenge 1:
# Given a 10x2 array of floats where the 1st column contains some nan values,
# create a 3rd column equal to column 1 where it's not nan and column 2 where it
# is nan. In other words, set column 3 equal to column 1, but fall back on
# column 2 where column 1 has a missing value.

# Setup
np.random.seed(123)
foo = np.random.uniform(low=0.0, high=1.0, size=(10, 2))
foo[np.random.randint(low=0, high=10, size=5), np.repeat(0, 5)] = np.nan
foo = np.round(foo, 2)
# Solution:
out3 = np.where(~np.isnan(foo[:, 0]), foo[:, 0], foo[:, 1])
out = np.concatenate((foo, out3.reshape((len(out3), 1))), axis=1)
print(out)

# %% Challenge2:
# Given a 1d array of integers, identify the first three values < 10 and replace
# them with 0.

# Setup
moo = np.array([0, 15, 32, 11, 5, 5, 24, 99, 81, 3, 45, 9, 41])
# Solution:
ind = np.where(moo < 10)
moo[ind[0][:3]] = 0
print(moo)
# Gorm solution:
moo = np.array([0, 15, 32, 11, 5, 5, 24, 99, 81, 3, 45, 9, 41])
moo[(moo < 10).nonzero()[0][:3]]
print(moo)

# %% Challenge 3:
# Insert 10 random normal values into a 5x5 array of 0s at random locations.

# Setup
oof = np.zeros(shape=(5, 5))
# Solution:
size = 10
rand = np.round(np.random.normal(loc=0.0, scale=1.0, size=size), 2)
pos = np.random.choice(np.arange(0, 25, 1), size=size, replace=False)
dim1, dim2 = oof.shape
oof_1d = oof.reshape(dim1 * dim2)
oof_1d[pos] = rand
oof = oof_1d.reshape((dim1, dim2))
print(oof)
# Alternative:
oof.ravel()[pos] = rand
print(oof)

# %% Challenge 4:
# Given peanut, a 4x5 array of 0s, and butter, a 5-element array of indices,
# fill the rows of peanut with 1s starting from the column indices given by
# butter.

# Setup
peanut = np.zeros(shape=(4, 5))
butter = np.array([3, 0, 4, 1])
# Solution
for i in range(len(butter)):
    peanut[i][butter[i]::] = 1
print(peanut)
# Alternative
(butter[:, None] <= np.arange(peanut.shape[1])).astype('int')

# %% Challenge 5:
# Given an array of integers, one hot encode it into a 2d array.

# Setup
yoyoyo = np.array([3, 1, 0, 1])
# Solution:
size = np.max(yoyoyo) + 1
(yoyoyo[:, None] == np.arange(size)).astype('int')
# Gorm 1:
result = np.eye(size)[yoyoyo]
print(result)
# Gorm 2:
result = np.zeros(shape=(len(yoyoyo), size))
result[np.arange(result.shape[0]), yoyoyo] = 1
print(result)
