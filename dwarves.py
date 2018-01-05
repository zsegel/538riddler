"""
Riddler Classic problem found here: 
https://fivethirtyeight.com/features/where-will-the-seven-dwarfs-sleep-tonight/

Each of the seven dwarfs sleeps in his own bed in a shared dormitory. Every night, they 
retire to bed one at a time, always in the same sequential order, with the youngest dwarf 
retiring first and the oldest retiring last. On a particular evening, the youngest dwarf 
is in a jolly mood. He decides not to go to his own bed but rather to choose one at 
random from among the other six beds. As each of the other dwarfs retires, he chooses his 
own bed if it is not occupied, and otherwise chooses another unoccupied bed at random.

    Q: What is the probability that the oldest dwarf sleeps in his own bed?
    A: A little less than 42%

    Q: What is the expected number of dwarfs who do not sleep in their own beds?
    A: About 4.142
"""
import numpy as np

def sim_one():
    beds = np.zeros(7)
    beds[np.random.randint(1, 7)] = 1  # put the first dwarf in someone else's bed
    own_bed_count = 0
    for d in range(2, 8):
        if not beds[d-1]:  # each dwarf sleeps in his own bed if it's unoccupied
            beds[d-1] = d
            own_bed_count += 1
        else:
            empty_beds = np.where(beds == 0)[0]
            beds[np.random.choice(empty_beds)] = d
    return own_bed_count, beds[6] == 7

def sim_many(n):
    own_bed_counts = []
    oldest_in_own_bed_count = 0
    for i in range(n):
        own_bed, oldest_in_own_bed = sim_one()
        own_bed_counts.append(own_bed)
        oldest_in_own_bed_count += oldest_in_own_bed
    return oldest_in_own_bed_count/float(n), np.mean(own_bed_counts)
    
    
print sim_many(500000)
