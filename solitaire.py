"""
While killing some time at your desk one afternoon, you fire up a new game of 
Solitaire (also called Klondike, and specifically the version where you deal out 
three cards from the deck at a time). But your boredom quickly turns to rage because 
your game is unplayable — you can flip through your deck, but you never have any 
legal moves! What are the odds?
"""


import numpy as np

class Simulator(object):    
    def __init__(self):
        self.d = {         # directed graph linking each card to
            2 : [29, 42],  # the cards that it can be placed on
            3 : [30, 43],
            4 : [31, 44],
            5 : [32, 45],
            6 : [33, 46],
            7 : [34, 47],
            8 : [35, 48],
            9 : [36, 49],
            10 : [37, 50],
            11 : [38, 51],
            12 : [39, 52],
            13 : [],
            15 : [29, 42],
            16 : [30, 43],
            17 : [31, 44],
            18 : [32, 45],
            19 : [33, 46],
            20 : [34, 47],
            21 : [35, 48],
            22 : [36, 49],
            23 : [37, 50],
            24 : [38, 51],
            25 : [39, 52],
            26 : [],
            
            # other color
            28 : [3, 16],
            29 : [4, 17],
            30 : [5, 18],
            31 : [6, 19],
            32 : [7, 20],
            33 : [8, 21],
            34 : [9, 22],
            35 : [10, 23],
            36 : [11, 24],
            37 : [12, 25],
            38 : [13, 26],
            39 : [],
            41 : [3, 16],
            42 : [4, 17],
            43 : [5, 18],
            44 : [6, 19],
            45 : [7, 20],
            46 : [8, 21],
            47 : [9, 22],
            48 : [10, 23],
            49 : [11, 24],
            50 : [12, 25],
            51 : [13, 26],
            52 : [],
        }

        
    def sim_one(self):
        """
        Simulates the start of one solitaire game.
        Returns True if the game is unplayable, False otherwise.
        """
        
        deck = np.arange(1, 53)
        np.random.shuffle(deck)
        
        cards = deck[:15]
        board = deck[:7]
        aces = [1, 14, 27, 40]
        
        for a in aces:
            if a in cards:
                return False
        
        for card in cards:
            for c in self.d[card]:
                if c in board:
                    return False
        
        return True
    
    
    def sim_many(self, n=1000000):
        """Monte Carlo simulation"""
        
        count = 0
        for i in range(n):
            count += self.sim_one()
        return count/float(n)

    
simulator = Simulator.()
print simulator.sim_many()
