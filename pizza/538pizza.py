# You and your two older siblings are sharing two extra-large 
# pizzas and decide to cut them in an unusual way. You overlap 
# the pizzas so that the crust of one touches the center of the 
# other (and vice versa since they are the same size). You then 
# slice both pizzas around the area of overlap. Two of you will 
# each get one of the crescent-shaped pieces, and the third will 
# get both of the football-shaped cutouts.

# Which should you choose to get more pizza: one crescent or two footballs?


###############################################################
###############################################################


# Here's a Monte Carlo approach to calculating the areas.
# I've assumed that the radius of each pizza is 1.
# One pizza's center is at the origin. the other pizza's
# center is at (1, 0).

# Equation for pizza at the origin: 1 = x**2 + y**2
# Equation for pizza centered at (1, 0): 1 = (x - 1)**2 + y**2

import numpy as np
import random
import matplotlib.pyplot as plt



def random_point():
    '''Generates a random (x, y) point in 
    a 2x2 square centered at the origin.
    '''
    signs = [1, -1]
    x = np.random.rand() * random.choice(signs)
    y = np.random.rand() * random.choice(signs)
    return x, y



points_to_generate = 100000

points_in_football = 0
points_in_crescent = 0

football_xs = []
football_ys = []

crescent_xs = []
crescent_ys = []



for i in range(points_to_generate):
    x, y = random_point()
    if x**2 + y**2 < 1:              #i.e., "if the point is in the pizza..."
        if (x - 1)**2 + y**2 < 1:    #i.e., "if the point is in the football..."            
            points_in_football += 1
            football_xs.append(x)
            football_ys.append(y)
        else:
            points_in_crescent += 1
            crescent_xs.append(x)
            crescent_ys.append(y)  



# The ratio of the number of points in the football to the 
# number of total points is approximately equivalent to the
# ratio of the area of the football to the area of the
# square (which is 4). That is:
#
#     pts in football / total pts == area of football / 4
#
# So the approximate area of one football is:

approx_one_football = (points_in_football/float(points_to_generate)) * 4
approx_two_footballs = 2 * approx_one_football


# The same logic applies to the crescent:
approx_one_crescent = (points_in_crescent/float(points_to_generate)) * 4


# I also calculated the actual areas analytically (see PDF):
actual_two_footballs = (4*np.pi - 3*np.sqrt(3)) / 3.
actual_one_crescent = (2*np.pi + 3*np.sqrt(3)) / 6.



print ""
print "AREA OF TWO FOOTBALLS"
print "   estimate:", approx_two_footballs
print "     actual:", actual_two_footballs
print ""
print "AREA OF ONE CRESCENT"
print "   estimate:", approx_one_crescent
print "     actual:", actual_one_crescent
print ""


plt.plot(crescent_xs, crescent_ys, 'ro')
plt.plot(football_xs, football_ys, 'bo')
plt.show()



# sample output
'''
AREA OF TWO FOOTBALLS
   estimate: 2.4568
     actual: 2.45673939722

AREA OF ONE CRESCENT
   estimate: 1.91768
     actual: 1.91322295498
'''
