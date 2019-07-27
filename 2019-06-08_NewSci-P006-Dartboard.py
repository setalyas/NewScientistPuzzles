# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 01:13:29 2019

@author: setat
"""

# =============================================================================
# What's the lowest score that you can't get with three darts?
# What's the lowest score that you can't get with two darts? One?
# N.B. can get zero by missing the board.
# =============================================================================

import numpy as np

singles = np.arange(0,21)
doubles = singles * 2
triples = singles * 3
bullseyes = np.array([25,50])
onedart = np.concatenate((singles,doubles,triples,bullseyes))
onedart = np.unique(onedart)
not1dart = [x for x in range(max(onedart)+1) if float(x) not in onedart]
print('lowest not possible with 1:',min(not1dart))
        
twodarts = np.array([])
for i in onedart:
    for j in onedart:
        twodarts = np.append(twodarts,i+j)
not2darts = [x for x in range(180+1) if float(x) not in twodarts]
print('lowest not possible with 2:',min(not2darts))

threedarts = np.array([])
for i in onedart:
    for j in onedart:
        for k in onedart:
            threedarts = np.append(threedarts,i+j+k)
            threedarts = np.unique(threedarts)
not3darts = [x for x in range(180+1) if float(x) not in threedarts]
print('lowest not possible with 3:',min(not3darts))