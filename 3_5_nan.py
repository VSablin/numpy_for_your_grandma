# In this script, we go through lesson 3.5 of Python NumPy for your
# Grandma course: nan. Web link here:
# https://www.gormanalysis.com/blog/python-numpy-for-your-grandma-nan/

# %% Import libraries

import numpy as np
# %% nan:
# nan is a float constant reserved to missing values.
# Example:
bot = np.ones(shape=(3, 4))
bot[[0, 2], [1, 2]] = np.nan
print(bot)
# Careful, if you want to find all the nan's, you must not use logical
# conditions. See this example:
bot == np.nan
# This is because np.nan is such that np.nan == np.nan is False. To find np.nan,
# use instead np.isnan():
np.isnan(bot)
# REMARK: np.nan is float. If you try to introduce np.nan in an integer or
# string array, you'll get an error:
foo = np.array([1, 2, 3], dtype='int64')
foo[1] = np.nan
