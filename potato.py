"""
Solution to the riddler express problem here: 
https://fivethirtyeight.com/features/is-this-bathroom-occupied/
"""

import numpy as np


def one_game():
    """Simulates one potato-coin game and returns the position of the winner."""

    # Children are numbered 0 to 29.
    children = range(30)  
     
    # Child 0 starts with the potato  	
    position = 0
    have_held_potato = [0]
    
    def pass_potato(position):
        """Flips a coin and passes the potato right or left."""
        
        if np.random.rand() < .5:
            # pass it to the right
            return (position+1) % 30
        else:
            # pass it to the left
            return (position-1) % 30
    
    while len(have_held_potato) != 29:
        position = pass_potato(position)
        if position not in have_held_potato:
            have_held_potato.append(position)
    else:
        winner = [x for x in children if x not in have_held_potato]
        return winner[0]

     
# Simulating the game 100,000 times        
results = [0] * 30

for i in range(100000):
    winner = one_game()
    results[winner] += 1

print results


"""
Sample results:
[0, 3489, 3479, 3369, 3456, 3386, 3538, 3415, 3434, 3429, 3496, 3414, 3452, 3534, 3411, 
3345, 3408, 3485, 3419, 3461, 3472, 3425, 3389, 3462, 3484, 3480, 3542, 3414, 3420, 3492]

These results indicate that each child has an equal shot at winning the game. (Except for
child who starts with the potato; they have no chance at winning!)
"""
