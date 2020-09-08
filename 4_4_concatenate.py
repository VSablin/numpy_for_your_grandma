# In this script, we go through lesson 4.4 of Python NumPy for your
# Grandma course: concatenate. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-concatenate/

# %% Import libraries

import numpy as np
# %% concatenate
# concatenate can be used to concatenate several arays. It takes a tuple or list
# of arrays as a first argument and axis=n as the axis to combine arrays along,
# being axis=0 the default value. Let's see some examples:
roux = np.zeros(shape=(3, 2))
gumbo = np.ones(shape=(2, 2))
# Let's combine roux with itself row-wise:
np.concatenate((roux, roux, roux), axis=0)
# or column-wise:
np.concatenate((roux, roux, roux), axis=1)
# Let's combine roux and gumbo row-wise:
np.concatenate((roux, gumbo), axis=0)
# arrays to be concatenated must have the same dimensions except the axis along
# we are concatenating. Otherwise, we get an error:
np.concatenate((roux, gumbo), axis=1)
