# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:23:40 2019

@author: SWannell
"""

import numpy as np
import matplotlib.pyplot as plt

size = 100000
x = np.random.ranf(size)
y = np.random.ranf(size)
diff = []
for i in range(size):
    n = abs(x[i] - y[i])
    diff.append(n)

diff = np.sort(diff)
dmean = diff.mean()
invdmean = 1 - dmean
print('p(candles on different slices)=',"%.3f" % dmean,
'\np(candles on different slices)=',"%.3f" % invdmean) 