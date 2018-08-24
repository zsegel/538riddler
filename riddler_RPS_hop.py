import numpy as np

"""
Solution to August 24th Riddler (fivethirtyeight.com/features/how-many-hoops-will-kids-jump-through-to-play-rock-paper-scissors/)

    Let’s call this game rock-paper-scissors-hop. Here is an idealized list of its rules:

    Kids stand at either end of N hoops. At the start of the game, one kid from each 
    end starts hopping at a speed of one hoop per second until they run into each other, 
    either in adjacent hoops or in the same hoop.

    At that point, they play rock-paper-scissors at a rate of one game per second until 
    one of the kids wins.

    The loser goes back to their end of the hoops, a new kid immediately steps up at that 
    end, and the winner and the new player hop until they run into each other.

    This process continues until someone reaches the opposing end. That player’s team wins!

    You’ve just been hired as the gym teacher at Riddler Elementary. 
    You’re having a bad day, and you want to make sure the kids stay 
    occupied for the entire class. 

    If you put down eight hoops, how long on average will the game last? 
    How many hoops should you put down if you want the game to last for 
    the entire 30-minute period, on average?


The code below uses a Monte Carlo simulation to estimate the expected duration
of a game of rock-paper-scissors hop played with N hoops.

Here are some example outputs:

    >>> sim_many(1, 40000)
    2.5010750000000002

    >>> sim_many(2, 40000)
    7.5054499999999997

    >>> sim_many(3, 60000)
    13.530033333333334

    >>> sim_many(4, 100000)
    20.471150000000002

    >>> sim_many(5, 100000)
    28.59093

    >>> sim_many(6, 200000)
    37.453785000000003

This follows a pretty easy-to-identify pattern:

N     E[N]
1 --> 2.5
2 --> 7.5  = 2.5 + (5) 
3 --> 13.5 = 2.5 + (5 + 6)
4 --> 20.5 = 2.5 + (5 + 6 + 7)
5 --> 28.5 = 2.5 + (5 + 6 + 7 + 8)
6 --> 37.5 = 2.5 + (5 + 6 + 7 + 8 + 9)
...
N -------> = 2.5 + (5 + 6 + ... + (N+2) + (N+3))

We can do a little math and write E[N] as a function of N:

    E[N] = 0.5*((N + 8)*(N - 1) + 5)
    
So...
A game with 8 hoops lasts 58.5 seconds on average.
And game with 57 hoops would last a little more than 30 minutes on average.

Here's the code:
"""

def sim_one(N):
    """Simulates one round of RPS hop played with N hoops."""
    
    time = 0
                    
    A = 0     # starting position of team A (to the left of hoop 1)
    B = N+1   # starting position of team B (to the right of hoop N)
    
    while True:        
        distance = (B - A) // 2  # the number of hoops each side moves before RPS
        A += distance
        B -= distance
        time += distance  # cuz we're moving at 1 hoop per second
        
        if ((A == 0) or (B == N+1)):  # game is over when either:
            return time               #    A is in hoop 30 and wins RPS
                                      #    B is in hoop 1 and wins RPS
        while True:
            RPS = np.random.random()
            time += 1
            if RPS <= (1/3.):   # B wins a third of the time
                A = 0
                break
            elif RPS <= (2/3.): # A wins a third of the time
                B = N+1
                break
                                # a third of the time they tie and throw again        
    
def sim_many(N, sims):
    """Uses Monte Carlo sim to estimate mean time of a RPS-hop game with N hoops"""
    
    results = []
    for i in range(sims):
        results.append(sim_one(N))
    return np.mean(results)
