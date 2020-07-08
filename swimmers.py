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
Answer: for five lanes, the expected number of swimmers is 2.466666... 
- There's a (2/5) chance that the first swimmer chooses lane 2 or 4, which each guarantee 
  that there will only be two swimmers. 
- There's a (1/5) chance that the first swimmer chooses lane 3, which guarantees that there
  will be three swimmers.
- There's a (2/5) chance that the first swimmer chooses lane 1 or 5. After that, there's a 
  (2/3) chance that the next swimmer chooses either lane three or the other lane at the end,
  in which case there will be three swimmers, and there is a (1/3) chance that the next swimmer
  chooses the lane that's next to the lane at the end, in which case there will be two swimmers.
- So the overall expected number of swimmers is: 
       (2/5)*2 + (1/5)*3 + (2/5)(2/3)*3 + (2/5)(1/3)*2 = (37/15) = 2.466666...

Extra credit: There's a linear relationship between the number of lanes, N,  and the expected
number of swimmers. Roughly, expected number of swimmers = 0.432*N + 0.3

"""
