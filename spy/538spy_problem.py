'''
Solution to the problem described here:
https://fivethirtyeight.com/features/how-much-is-a-spy-worth-in-a-warring-riddler-nation/
'''

import numpy as np
import itertools
import random
import matplotlib.pyplot as plt

class SpyEvaluator(object):
    """A helpful tool for solving the spy problem."""
    
    def __init__(self):
        """This basically just populates a list called 'ways_to_win' with all possible 
        ways to win in a head-to-head matchup (i.e., score more than 27.5 points). This
        list is used by the min_soldiers_needed function below.
        
        Examples: (W, L, L, L, L, L, L, W, W, W) is one way to win; it's worth 28 points.
                  (W, W, W, W, T, W, T, L, L, W) is another; it's worth 32 points.
        """
        ways_to_win = []
        for outcome in list(itertools.product(('W', 'L', 'T'), repeat=10)):
            points = 0
            for i in range(10):
                if outcome[i] == 'W':
                    points += i+1
                elif outcome[i] == 'T':
                    points += (i+1) / 2.
            if points > 27.5:
                ways_to_win.append(outcome)
        self.ways_to_win = ways_to_win
        
    def min_soldiers_needed(self, enemy_dist):
        """Figures out minimum number of soldiers needed to beat a distribution.
        
        Args:
            enemy_dist (list): Ten ints representing the enemy's distribution.
            
        Returns:
            int: The minimum number of soldiers needed to win.
            list: The way to distribute those soldiers.
        """
        minimum = 100
        my_winning_dist = []
        for way in self.ways_to_win:
            soldiers = 0
            my_dist = []
            for i in range(10):
                if way[i] == 'W':
                    soldiers += enemy_dist[i]+1
                    my_dist.append(enemy_dist[i]+1)
                elif way[i] == 'T':
                    soldiers += enemy_dist[i]
                    my_dist.append(enemy_dist[i])
                else:
                    my_dist.append(0)
            if soldiers < minimum:
                my_winning_dist = my_dist
                minimum = soldiers
        return minimum, my_winning_dist
    
    def futz(self, dist, n=25, depth=5):
        """Our goal is to find an enemy distribution that requires the greatest minimum 
        number of soldiers to defeat.
        
        This function takes an enemy distribution and then futzes with it randomly to see 
        if an enemy distribution similar to it requires more soldiers to defeat. If it 
        finds one, it starts futzing with THAT distribution, etc.
        
        Technically speaking, this is a very clunky form of stochastic optimization. 
        We're trying to find the maximum of the min_soldiers_needed function.
        
        Args:
        	dist (list): The distribution you start futzing with (10 ints).
        	n (int): The number of times you futz.
        	depth (int greater than 1): The amount of futziness per futz.
        	
        Returns:
        	int: Greatest output value of the min_soldiers_needed function that it found.
        	list: Distribution of soldiers that produces that output value.
        	list: A record of the optimization over time.
        """
        candidate = dist
        target = self.min_soldiers_needed(candidate)[0]
        targets = [target]
        
        for i in range(n):
            new_candidate = candidate[:]
            for i in range(0, np.random.randint(1, depth)):
                decrease = np.random.randint(10)
                while new_candidate[decrease] == 0: 
                    decrease = np.random.randint(10)
                increase = np.random.randint(10)
                new_candidate[decrease] -= 1
                new_candidate[increase] += 1
                
            if self.min_soldiers_needed(new_candidate)[0] > target:
                target = self.min_soldiers_needed(new_candidate)[0]
                targets.append(target)
                candidate = new_candidate[:]
            else:
                targets.append(target)
        return self.min_soldiers_needed(candidate)[0], candidate, targets
        

# We can use the SpyEvaluator to find the solution to the problem.

evaluator = SpyEvaluator()
starting_dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
end, end_dist, targets = evaluator.futz(starting_dist, 25000)

print 'minimum soldiers needed to beat any distribution:', end
print 'enemy distribution that is hardest to beat:', end_dist
plt.plot(targets)
plt.show()

# This algorithm finds the maximum (which is 56) after about 15,000 rounds of futzing.
# The minimum number of soldiers needed to beat any possible distribution is 56.
# The enemy distribution that is hardest to beat is [1, 3, 5, 7, 9, 11, 13, 15, 17, 19].
