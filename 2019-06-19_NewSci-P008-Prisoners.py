# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 00:49:09 2019

@author: setat
"""

# =============================================================================
# 40 prisoners in 40 cells, 40 guards
# All cells start open
# Each guard takes a number n in 1-40, and turns key of each n and multiple of n
# At the end, the warden turns all the keys
# 1 turn = locked. 2 turns = unlocked etc.
# =============================================================================

# Revelation 1 - it's independent of the order
# Revelation 2 - as each n has an even number of divisors, they'll all end locked??

import numpy as np

prison = 40
doorsLocked = np.zeros(prison, dtype=bool) # open is zero, closed is 1

# Guards do their thing
for key in np.arange(1,prison+1):
    for door in np.arange(key,prison+1):
        if door % key == 0:
            k = key-1
            doorsLocked[door-1] = not(doorsLocked[door-1])
#        print('key',key,'\ndoor=',door,'\ndoors=',doorsLocked)

#firstPassLocked = [i+1 for i in range(len(doorsLocked)) if doorsLocked[i]]
#print('locked after first pass',firstPassLocked)
        
# warden turning all the keys
doorsLocked = [not b for b in doorsLocked]
free = [i+1 for i in range(len(doorsLocked)) if not doorsLocked[i]]

print('Free by the end',free)