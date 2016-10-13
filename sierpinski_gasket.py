# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:38:42 2016

@author: A. Orden
"""

import numpy as np
import matplotlib.pyplot as plt
from random import random, randint

# Select three points p1, p2 and p3 and a starting point
p1 = [random()*2, random()*-1]
p2 = [random()*1, random()*3]
p3 = [random()*-1, random()*1]
q = [random(), random()]

xlist = [q[0]]
ylist = [q[1]]

iterations = 100000

for _ in xrange(iterations):
    # Randomly (by casting a die) pick one of the three points pi
    i = randint(1,3)

    # Determine the center of the line connecting q and pi
    if i == 1:
        qx = (q[0] + p1[0]) / 2.
        qy = (q[1] + p1[1]) / 2.
    if i == 2:
        qx = (q[0] + p2[0]) / 2.
        qy = (q[1] + p2[1]) / 2.
    if i == 3:
        qx = (q[0] + p3[0]) / 2.
        qy = (q[1] + p3[1]) / 2.

    # Assign q_{n+1} as the new q_n
    q = [qx, qy]
    
    xlist.append(q[0])
    ylist.append(q[1])
    
plt.plot(xlist, ylist, 'o')
plt.xlim([min(xlist), max(xlist)])
plt.ylim([min(ylist), max(ylist)])
plt.show()