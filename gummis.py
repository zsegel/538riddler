import numpy as np

gummis = np.random.shuffle([0]*30 + [1]*30)

A = 0
B = 0
for i in range(15):
  four = gummis[i*4:i*4 + 4]
  if four.coun
