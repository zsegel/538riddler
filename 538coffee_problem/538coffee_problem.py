# Riddler Headquarters is a buzzing hive of activity. 
# Mathematicians, statisticians and programmers roam 
# the halls at all hours, proving theorems and calculating 
# probabilities. They’re fueled, of course, by caffeine. 
# But the headquarters has just one coffee pot, along with 
# one unbreakable rule: You finish the joe, you make some mo’.

# Specifically, the coffee pot holds one gallon of coffee, and 
# workers fill their mugs from it in sequence. Whoever takes 
# the last drop has to make the next pot, no ifs, ands or buts. 
# Every worker in the office is trying to take as much coffee 
# as he or she can while minimizing the probability of having 
# to refill the pot. Also, this pot is both incredibly heavy 
# and completely opaque, so it’s tough to tell how much remains. 
# That means a worker can’t keep pouring until she sees or feels 
# just a drop left. Anyone stuck refilling the pot becomes so 
# frustrated that they throw their cup to the ground in frustration, 
# so they get no coffee that round.

# Congratulations! You’ve just been hired to work at Riddler Headquarters. 
# Submit a number between 0 and 1. (It could be 0.9999, or 0.0001, or 0.5, 
# or 0.12345, and so on.) This is the number of gallons of coffee you will 
# attempt to take from the pot each time you go for a cup. If that amount 
# remains, lucky you, you get to drink it. If less remains, you’re out of 
# luck that round; you must refill the pot, and you get no coffee.

# Once I’ve received your submissions, I’ll randomize the 
# order in which you and your colleagues head for the pot. 
# Then I’ll run a lot of simulations — thousands of hypothetical 
# trips to the coffee pot in the Riddler offices. Whoever drinks 
# the most coffee is the ☕ Caffeine King or Queen ☕ of Riddler Headquarters!



# below is some of the code I wrote to explore this problem!


import random
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline #I did all this in an iPython notebook...




class Worker(object):
    
    def __init__(self, pour_size):
        self.pour_size = pour_size
        self.coffee_consumed = 0
        self.pots_refilled = 0

    def get_coffee(self, coffee_pot):
        if self.pour_size <= coffee_pot:
            self.coffee_consumed += self.pour_size
            coffee_pot -= self.pour_size
            return coffee_pot
        else:
            self.pots_refilled += 1
            coffee_pot = 1
            return coffee_pot




def simulate_one_game(workers):
    #put workers in random order
    random.shuffle(workers)
    
    #fill up the coffee pot to start
    coffee_pot = 1
    
    for i in range(len(workers)):
        coffee_pot = workers[i].get_coffee(coffee_pot)


def simulate_many_games(workers, number_of_sims=20000):
    
    for i in range(number_of_sims):
        simulate_one_game(workers)
    
    total_coffee_consumed = 0
    total_pots_refilled = 0
    
    for w in workers:
        total_coffee_consumed += w.coffee_consumed
        total_pots_refilled += w.pots_refilled
    
    #sort workers by coffee_consumed
    workers.sort(key=lambda w: w.coffee_consumed, reverse=True)
    
    ranked_pour_sizes = []
    for w in workers:
        ranked_pour_sizes.append(w.pour_size)
    
    return ranked_pour_sizes






#functions for creating batches of workers

def make_workers_uniform(n):
    #makes workers whose pour_sizes are drawn from a uniform distribution    
    pours = np.random.random(n)
            
    workers = []
    for p in pours:
        workers.append(Worker(p))
        
    return workers


def make_workers_normal(n, mean, std_dev):
    #makes workers whose pour_sizes are drawn from a gaussian distribution
    pours = np.random.normal(mean, std_dev, n)
                
    workers = []
    for p in pours:
        workers.append(Worker(p))
        
    return workers





###################################################################
###################################################################
###################################################################


#OBSERVATION ONE

# When workers' pour sizes are drawn from a uniform distribution,
# larger pour sizes do better. There is some noise in the top 
# quintile, though. 

thousand_random_workers = make_workers_uniform(1000)
ranked_pour_sizes1 = simulate_many_games(thousand_random_workers)


#example of code used to plot results
plt.plot(ranked_pour_sizes1)
plt.xlabel('coffee consumed rank')
plt.ylabel('pour size')



#OBSERVATION TWO

# Larger pour sizes perform better when workers' pour sizes
# are clustered around 0.3, 0.6, and 0.9 in three equally-sized
# groups.

workers1 = make_workers_normal(333, 0.3, 0.05)
workers2 = make_workers_normal(333, 0.6, 0.05)
workers3 = make_workers_normal(333, 0.9, 0.03)
workers = workers1 + workers2 + workers3
workers.append(Worker(1.0)) #this worker wins pretty much every time

ranked_pour_sizes2 = simulate_many_games(workers)




#OBSERVATION THREE

# Trying to take a lot of coffee is not always a
# dominant strategy, though. Here's a situation where 
# three-fourths of workers are clustered around 0.25, about 
# one-fourth is clustered around 0.45, and a handful try to 
# take a gallon every time. These whole-gallon players
# (represented by vertical spikes around rank ~260 on the 
# accompanying graph) don't win.

workers1 = make_workers_normal(750, 0.25, 0.1)
workers2 = make_workers_normal(245, 0.45, 0.1)
workers3 = make_workers_normal(5, 1, 0)
workers = workers1 + workers2 + workers3

ranked_pour_sizes3 = simulate_many_games(workers)




#OBSERVATION FOUR

# If enough players go for the whole pot every time, they all
# end up performing well. Here's a case where four-fifths of 
# workers' pour sizes are drawn from a normal distribution with
# mean 0.5, and one-fifth of workers go for the pot every time.

workers1 = make_workers_normal(800, 0.5, 0.15)
workers2 = make_workers_normal(200, 1, 0)
ranked_pour_sizes4 = simulate_many_games(workers)
#the whole-gallon players take the top 200 spots.




#OBSERVATION FIVE

# Even if only 5% of players try to take the whole pot, they still
# perform better than most (or all) other players, especially if those
# other players' average pour size is closer to 1 than to 0.


workers1 = make_workers_normal(950, 0.9, 0.03) #950 workers' pours are clustered around 0.9
workers2 = make_workers_normal(50, 1, 0)
workers = workers1 + workers2
ranked_pour_sizes5a = simulate_many_games(workers)
# all the ones who take the whole pot perform better than all others


workers1 = make_workers_normal(950, 0.7, 0.1) #950 workers' pours are clustered around 0.7
workers2 = make_workers_normal(50, 1, 0)
workers = workers1 + workers2
ranked_pour_sizes5b = simulate_many_games(workers)
# all the ones who take the whole pot perform better than all others


workers1 = make_workers_normal(950, 0.5, 0.1) #950 workers' pours are clustered around 0.5
workers2 = make_workers_normal(50, 1, 0)
workers = workers1 + workers2
ranked_pour_sizes5c = simulate_many_games(workers)
# all the ones who take the whole pot perform better than all others



#CONCLUSION

# Even though going for the whole pot every time doesn't guarantee a win,
# it's a strategy that generally performs well, especially if other co-workers
# also go for the whole pot every time.


