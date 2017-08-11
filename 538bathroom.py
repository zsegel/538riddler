'''
Solution to the Riddler classic problem here:
https://fivethirtyeight.com/features/is-this-bathroom-occupied/
'''

import numpy as np


def bathroom(p_consc=1/3., sims=1000000):
    """Estimates proportion of time that 'vacant' and 'occupied' signs are accurate.
    
    Args:
        p_consc (float): proportion of users that are conscientious
        sims (int): number of simulated trips to the bathroom
        
    Returns:
        float: estimated proportion of time 'occupied' sign is accurate
        float: estimated proportion of time 'vacant' sign is accurate
    """

    # initialize time counts
    occupied_true = 0
    occupied_false = 0
    vacant_true = 0
    vacant_false = 0
    
    # initialize sign
    sign = "vacant"
    
    # determine p of oblivious users, i.e., users who never change the sign
    p_oblivious = (1 - p_consc)/2.
    
    for i in range(sims):
        u = np.random.rand()
        
        if u < p_consc: # conscientious user
            occupied_true += 1
            vacant_true += 1
            sign = "vacant"
        
        elif u < p_consc + p_oblivious: # oblivious user
            if sign == "vacant":
                vacant_false += 1
                vacant_true += 1
            else:
                occupied_true += 1
                occupied_false += 1
        
        else:
            occupied_true += 1
            occupied_false += 1
            sign = "occupied"
    
    
    return round(occupied_true/float(occupied_true + occupied_false), 3), round(vacant_true/float(vacant_true + vacant_false), 3)
    
answer = bathroom()

print "The probability that an 'occupied' sign is correct is:", answer[0]
print "The probability that a 'vacant' sign is correct is:", answer[1]


"""
Occupied signs are correct 5/6 of the time.
Vacant signs are correct 1/2 of the time.
"""
