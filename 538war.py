"""
Solution to Riddler Classic problem found here:
https://fivethirtyeight.com/features/riddler-nation-goes-to-war/

Consider a standard, two-player, 52-card game of War. If I start 
with just the four aces, and you start with all 48 other cards, 
randomly shuffled, what are your chances of winning?

The code below models the game as specified here: http://www.bicyclecards.com/how-to-play/war/
Any cards a player wins are added to the bottom of that player's pile in a random order."""

import numpy as np
from collections import deque

def sim_one_game():
    """returns True if the player who doesn't start with the aces wins"""
    
    # starting cards
    A = deque([14, 14, 14, 14])
    B = deque(range(2,14) * 4)
    np.random.shuffle(B)
    
    while len(A) and len(B):
        cards = [A.popleft(), B.popleft()]
        war = []

        while (cards[0] == cards[1]):
            war.extend(cards[:])
            try:
                war.extend([A.popleft(), B.popleft()])
                cards = [A.popleft(), B.popleft()]
            except:
                return bool(len(B))
     
        if cards[0] > cards[1]:
            cards.extend(war)
            np.random.shuffle(cards)
            A.extend(cards[:])
        else:
            cards.extend(war)
            np.random.shuffle(cards)
            B.extend(cards[:])
    else:
        return bool(len(B))

# Monte Carlo approximation of the probability that the non-ace player wins
sims = 100000
wins = 0
for i in range(sims):
    if sim_one_game():
        wins += 1
print wins/float(sims)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                           #
#   ANSWER: the probability that the non-ace player wins is about 19.3%     #
#                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
