
'''
Solution to Riddler Classic problem found here:
https://fivethirtyeight.com/features/riddler-nation-goes-to-war/

Consider a standard, two-player, 52-card game of War. If I start 
with just the four aces, and you start with all 48 other cards, 
randomly shuffled, what are your chances of winning?
'''

import numpy as np
from collections import deque

def sim_one_game():
    """returns True if player B wins"""

    A = deque([14, 14, 14, 14])
    
    B = deque(range(2,14) * 4)
    np.random.shuffle(B)
    
    while len(A) and len(B):
        rounds += 1
        cards = [A.popleft(), B.popleft()]
        war = []

        # war
        while (cards[0] == cards[1]):
            war.extend(cards[:])
            try:
                war.extend([A.popleft(), B.popleft()])
                cards = [A.popleft(), B.popleft()]
            except:
                return bool(len(B))
     
        # A wins
        if cards[0] > cards[1]:
            cards.extend(war)
            np.random.shuffle(cards)
            A.extend(cards[:])
        # B wins
        else:
            cards.extend(war)
            np.random.shuffle(cards)
            B.extend(cards[:])

    else:
        return bool(len(B))

