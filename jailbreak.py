
import numpy as np

class Prison(object):
    def __init__(self, prisoners):
        self.prisoners = prisoners
        self.lever_state = np.random.randint(4)
        self.order = list(np.random.randint(0, 100, 20000))
        self.game_over = False
        self.total_trips = 0
        
    def cell_zero(self):
        self.total_trips += 1
        try:
            prisoner = self.prisoners[self.order.pop()]
        except:
            # refill the random order list when it runs out
            self.order = list(np.random.randint(0, 100, 1000))
            prisoner = self.prisoners[self.order.pop()]
        
        self.lever_state = prisoner.flip_lever(self.lever_state)
        
        if self.lever_state == -1:
            self.game_over = True
    
    def jailbreak(self):
        while not self.game_over:
            self.cell_zero()
        else:
            return self.total_trips 
            

class Prisoner(object):
    def __init__(self, is_counter=False):
        self.trips_to_cell_zero = 0
        
        self.is_counter = is_counter
        if self.is_counter:
            self.count = 0
            self.count_next_2_to_0_flip = False
            
        else:
            self.has_flipped_1_to_3 = False
            self.has_seen_2_or_3 = False
            
    def flip_lever(self, lever_state):
        self.trips_to_cell_zero += 1
        
        # strategy for the one counter
        if self.is_counter:
            if lever_state == 0:
                return 1
                
            elif lever_state == 1:
                self.count_next_2_to_0_flip = False
                return 3
            
            elif lever_state == 3:
                return 2
                       
            elif lever_state == 2:
                if self.count_next_2_to_0_flip:
                    self.count += 1
                    if self.count == 99:
                        # this stops the game
                        return -1
                self.count_next_2_to_0_flip = True
                return 0
            
        # strategy for the 99 non-counters
        else:
            if lever_state == 0:
                return 1
            
            elif lever_state == 1:
                if self.has_seen_2_or_3 and not self.has_flipped_1_to_3:
                    self.has_flipped_1_to_3 = True
                    return 3
                else:
                    return 0
                
            elif lever_state == 3:
                self.has_seen_2_or_3 = True
                return 2
                
            elif lever_state == 2:
                self.has_seen_2_or_3 = True
                return 3


def sim_one():
    # create one counter
    prisoners = [Prisoner(is_counter=True)]
    
    # create 99 non-counters
    for i in range(99):
        prisoners.append(Prisoner())
    
    # put them in the prison
    prison = Prison(prisoners)
    
    # play the warden's jailbreak game
    return prison.jailbreak()

def sim_many(n):
    results = []
    for i in range(n):
        results.append(sim_one())
    return results
    

