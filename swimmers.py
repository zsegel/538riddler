"""
Riddler Express (3 July 2020)

It’s summertime and my local swimming pool, which has exactly five swimming lanes (and no general swim area), 
may be opening in the coming weeks. It remains unclear what social distancing practices will be required, but 
it’s quite possible that swimmers will not be allowed to occupy adjacent lanes.

Under these guidelines, the pool could accommodate at most three swimmers — one each in the first, third and 
fifth lanes.

Suppose a queue of swimmers arrives at the pool when it opens at 9 a.m. One at a time, each person randomly 
picks a lane from among the lanes that are available (i.e., the lane has no swimmer already and is not adjacent 
to any lanes with swimmers), until no more lanes are available.

At this point, what is the expected number of swimmers in the pool?

Extra credit: Instead of five lanes, suppose there are N lanes. When no more lanes are available, what is the 
expected number of swimmers in the pool?
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def sim_one(N):
    swimmers = 0
    lanes = np.ones(N)   # 1 means open, 0 means unavailable
    while np.sum(lanes):
        swimmers += 1
        lane = np.random.choice(np.nonzero(lanes)[0]) #randomly choose index of open lane
        lanes[lane] = 0  # block chosen lane
        if lane == 0:     # if first lane is chosen, block second lane
            lanes[1] = 0
        elif lane == N-1: # if last lane is chosen, block second to last lane
            lanes[N-2] = 0
        else:             # for all other lanes, block lanes on either side
            lanes[lane-1] = 0
            lanes[lane+1] = 0    
    return swimmers


def sim_many(N, sims=10000):
    '''monte carlo simulation to estimate the expected number of swimmers, given N lanes'''
    results = []
    for i in range(sims):
        results.append(sim_one(N))
    return np.mean(results)
    
    
xs = list(range(5,65))
ys = []
for x in xs:
	ys.append(sim_many(x))
	
y = np.array(ys)
X = np.array(xs).reshape(-1, 1)

model = LinearRegression()
model.fit(X, y)

print("slope:", model.coef_)
print("intercept", model.intercept_)

"""
Answer: for five lanes, the expected number of swimmers is about 2.466...

Extra credit: There's a linear relationship between the number of lanes, N,  and the expected
number of swimmers. Roughly, xxpected number of swimmers = 0.432*N + 0.3

"""
