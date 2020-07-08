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