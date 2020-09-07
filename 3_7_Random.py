# In this script, we go through lesson 3.7 of Python NumPy for your
# Grandma course: Random. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-random/

# %% Import libraries

import numpy as np
# %% Random:
# We will see how we can np random module to shuffle arrays, sample values from
# arrays, and draw values from probability distributions.
# E.g. let's simulate a 6-sided die. In particular, throwing three times the
# die:
np.random.randint(low=1, high=7, size=3)
# To generate reproducible research we must set a seed:
np.random.seed(2357)
np.random.randint(low=1, high=7, size=3)
np.random.randint(low=1, high=7, size=3)
np.random.seed(2357)
np.random.randint(low=1, high=7, size=3)
np.random.randint(low=1, high=7, size=3)
# What if we want to draw three values between 1 and 6 without replacement?
# We can use the choice() function, choice(a, size=None, replace=True, p=None),
# where the arguments are:
# 1) a: values from which to sample
# 2) size: number of samples
# 3) replace: should values be replaced?
# 4) p: probabilities corresponding to a
np.random.seed(2357)
# Example 1: 3 values from a 6-sided die without replacement:
np.random.choice(a=np.arange(1, 7),
                 size=3,
                 replace=False,
                 p=None)
# Example 2: 3 values from a biased 6-sided die without replacement:
np.random.choice(a=np.arange(1, 7), size=3, replace=False,
                 p=np.array([0.1, 0.1, 0.1, 0.1, 0.3, 0.3]))
# Example 3: 3 strings from 6 words without replacement:
np.random.choice(a=np.array(['you', 'can', 'use', 'strings', 'too']),
                 size=3,
                 replace=False,
                 p=None)
# You can also sample rows from a 2D array:
foo = np.array([[1, 2],
               [3, 4],
               [5, 6],
               [7, 8],
               [9, 10]])
np.random.seed(1234)
# We can use this by creating a np.array of random integers!
rand_rows = np.random.randint(low=0, high=foo.shape[0], size=3)
foo[rand_rows]
# If we want to avoid replacement, we must use choice with replace=False:
rand_rows = np.random.choice(a=np.arange(start=0, stop=foo.shape[0]),
                             replace=False,
                             size=3)
foo[rand_rows]
# We can use this to shuffle an array, but it's even easier with permutation:
np.random.permutation(foo)
# np allosw to sample numbers from several distributions:
# 1) Uniform distribution:
np.random.uniform(low=1.0, high=2.0, size=(2, 2))
# 2) Normal distribution:
np.random.normal(loc=0.0, scale=1.0, size=2)
# 3) Binomial distribution:
np.random.binomial(n=10, p=0.25, size=(3, 2))
# There are many more covered in the np documentation.
