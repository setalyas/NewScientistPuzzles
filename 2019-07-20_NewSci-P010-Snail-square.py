# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:34:01 2019

@author: SWannell
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([0,2])
B = np.array([2,2])
C = np.array([2,0])
D = np.array([0,0])

#print([A,B,C,D])

aLine = [A]
bLine = [B]
cLine = [C]
dLine = [D]

mult = 1

per_second = mult * 2 / (60*60)

def MoveTo(x,y,d=per_second):
    """Move d distance from x to y"""
    step = np.subtract(y,x)*d
    return x+step

def dist(x,y):
    """Distance from x to y"""
    return np.linalg.norm(y-x)

#Move til distance is < 1cm
t = 0
while dist(A,B) > 0.01:
    A = MoveTo(A,B)
    B = MoveTo(B,C)
    C = MoveTo(C,D)
    D = MoveTo(D,A)
    aLine.append(A)
    bLine.append(B)
    cLine.append(C)
    dLine.append(D)
    t += mult
print('time elapsed = ',divmod(9536,60*60)[0],"hrs",divmod(9536,60*60)[1]//60,"mins")

# minutes elapsed: 9537

#print([aLine,bLine,cLine,dLine])
   
plt.rcParams["figure.figsize"] = (5,5)
for line in [aLine,bLine,cLine,dLine]:
    plt.scatter(*zip(*line))
plt.show()

"""logarithmic spiral parameterised for C:
x(t) = 2 * e**(b*t) * math.cos(t)
y(t) = 2 * e**(b*t) * math.sin(t)

x=y=1 => t=(pi/4)+pi*k for some k => cos(t)=sin(t) = 1/np.sqrt(2)

=> e**(b*t) = np.sqrt(2) / 2
=> 
https://en.wikipedia.org/wiki/Mice_problem#Path_of_the_mice"""