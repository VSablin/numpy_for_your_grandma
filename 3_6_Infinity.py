# In this script, we go through lesson 3.6 of Python NumPy for your
# Grandma course: Infinity. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-infinity/

# %% Import libraries

import numpy as np
# %% Infinity:
# np reserves floating point constants to infinity or minutos infinity.
np.array([np.inf, np.NINF])
# You can get this dividing by 0:
np.array([-1, 1])/0
# As expected
np.inf * 22
np.inf + np.inf
np.inf - np.inf
np.inf/np.inf
# Booleans are allowed:
np.inf == np.inf
np.NINF == np.NINF
# So we can subset infinity values with booleans:
foo = np.array([4.4, np.inf, 1.0, np.NINF, 3.1, np.inf])
foo == np.inf
foo == np.NINF
