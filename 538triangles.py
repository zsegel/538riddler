"""
Solution to the Riddler Classic problem here: 
https://fivethirtyeight.com/features/will-you-be-a-ghostbuster-or-a-world-destroyer/

These problems are pretty straightforward once we realize the following:

Given stick lengths a, b, c, where a < b < c:
	I.  a, b, c can form a triangle iff a+b > c
	II. a, b, c can form an acute triangle iff a**2 + b**2 > c**2
	
We can use Monte Carlo simulations to get approximate answers to the questions:
	1. 50.00%
	2. 25.00%
	3.  7.95%
	4. 21.46%

And our work here is DONE. Code below."""

import numpy as np
sims = 1000000

count1 = 0
for i in range(sims):
    break1, break2 = sorted(np.random.random(2))
    a, b, c = sorted([break1, break2-break1, 1-break2])
    if a+b > c:
        count1 += 1
print "Answer to question 1:", count1/float(sims)

count2 = 0
for i in range(sims):
    a, b, c = sorted(np.random.random(3))
    if a+b > c:
        count2 += 1  
print "Answer to question 2:", count2/float(sims)

count3 = 0
for i in range(sims):
    break1, break2 = sorted(np.random.random(2))
    a, b, c = sorted([break1, break2-break1, 1-break2])
    if a**2 + b**2 > c**2:
        count3 += 1
print "Answer to question 3:", count3/float(sims)

count4 = 0
for i in range(sims):
    a, b, c = sorted(np.random.random(3))
    if a**2 + b**2 > c**2:
        count4 += 1
print "Answer to question 4:", count4/float(sims)
