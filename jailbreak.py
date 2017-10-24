"""
Solution to the Riddler Classic problem found here:
https://fivethirtyeight.com/features/can-you-please-the-oracle-can-you-escape-the-prison/

   'One hundred prisoners are put into 100 completely isolated cells, numbered 1 to 100. Once they are 
    in their cells, they cannot communicate with each other in any way. They are taken by the warden one 
    at a time, but in no particular order, to a special room, Cell 0, in which there are two levers. As 
    the prisoners enter the room, each lever is either up or down, but the levers’ starting positions are 
    unknown. When in the room, a prisoner must flip exactly one of the levers. At any point, any prisoner 
    may declare to the warden that all of the prisoners have been to the room. (The warden will take 
    prisoners to the room indefinitely until someone makes a guess.) If the prisoner is correct, they are 
    all released. If not, they are all executed.

    Knowing these rules, what strategy can the prisoners devise beforehand that will guarantee their release? 
    How many trips to Cell 0 will it take on average before they are released?'

I. A WINNING STRATEGY

Ok. There are four states the levers can be in: (down, down), (down, up), (up, down), and (up, up).

Let's give these states names:
    (down, down) --> STATE 0
    (down, up) ----> STATE 1
    (up, down) ----> STATE 2
    (up, up)   ----> STATE 3
    
Note that it is impossible for a single flip to move the levers from STATE 0 to STATE 3 (and vice versa), or 
from STATE 1 to STATE 2 (and vice versa). The state transitions connect to each other like this:

               STATE 1
               /     \
         STATE 0     STATE 3
               \     /
               STATE 2

Here's a strategy that will guarantee the prisoners' release:

    1. The prisoners choose one person to be the "counter." The counter is the only one who can declare
       that all the prisoners have visited cell zero.
    
    2. Everyone besides the counter flips the levers like this:
            STATE 0: always flip to STATE 1
            
            STATE 1:
                -only flip to STATE 3 if:
                    i.  they have never flipped STATE 1 to STATE 3
                    ii. they have seen the levers in STATE 2 or STATE 3
                -otherwise, flip STATE 1 to STATE 0
                
            STATE 2: always flip to STATE 3
            STATE 3: always flip to STATE 2
            
    3. The counter flips the levers like this:
            STATE 0: always flip to STATE 1
            STATE 1: always flip to STATE 3
            STATE 2: always flip to STATE 0
            STATE 3: always flip to STATE 2
            
    4. The counter counts the number of times they flip STATE 2 to STATE 0, except:
            i.  they don't count the first time they do it, 
            ii. they don't count it if they flipped STATE 1 to STATE 3 after 
                the last time they flipped STATE 2 to STATE 0.
    
    5. When the counter's count reaches 99, they declare that all prisoners have visited cell 0.
    
    
On average, this strategy requires the prisoners to make about 22,180 trips to cell zero before 
they're released.
    
   
            
            
II. WHY DOES THE STRATEGY WORK?

               STATE 1
              //     \
         STATE 0     STATE 3
               \     //
               STATE 2
              
Most of the time, the levers are bouncing back and forth between either STATE 0 and STATE 1 or
STATE 3 and STATE 2. Think of these as two "modes" that the system can be in:

               MODE A
              //     \
         MODE A     MODE B
               \    //
               MODE B 

When the system is in MODE A, it's waiting for a new prisoner to shift it into MODE B, and when 
it's in MODE B, it's waiting for the counter to shift it back to MODE A (something only the counter
can do).

Each prisoner only shifts the system from MODE A to MODE B once, so the counter counts the number 
of times a non-counter has shifted the system into that mode. When the counter's count reaches 99, 
they can be sure that all prisoners have been to cell zero.

Because the initial state of the levers is unknown, the non-counters aren't allowed to shift the
system from MODE A to MODE B until they've already seen it in MODE B. Suppose they didn't do this. 
The first time the counter visits cell zero, if the system is in MODE B, it'll be unclear which mode
it started in--did it start in MODE A and get shifted to MODE B by another prisoner, or did it
start in MODE B? This is a problem. When the counter shifts the system back into MODE A, should they 
add 1 to their count?

Because the non-counters aren't allowed to shift the system to MODE B until they've already seen it in
MODE B, the counter can be sure that the first mode they see the system in is the mode it started in.
(If it starts in MODE A, only the counter is allowed to shift it into MODE B.)

The counter always shifts the system from MODE A to MODE B when they can for simplicity's sake. The
strategy would still work if they only shifted it from MODE A to MODE B some of the time.
"""

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
        self.is_counter = is_counter
        if self.is_counter:
            self.count = 0
            self.count_next_2_to_0_flip = False
        else:
            self.has_flipped_1_to_3 = False
            self.has_seen_2_or_3 = False
            
    def flip_lever(self, lever_state):
        # counter's strategy
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
                        return -1   # this stops the game
                self.count_next_2_to_0_flip = True
                return 0
            
        # non-counters' strategy
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


# SIMULATING THE JAILBREAK GAME REPEATEDLY
def sim_one():
    # create one counter
    prisoners = [Prisoner(is_counter=True)]
    
    # create 99 non-counters
    for i in range(99):
        prisoners.append(Prisoner())
    
    prison = Prison(prisoners)
    
    return prison.jailbreak()

def sim_many(n):
    results = []
    for i in range(n):
        results.append(sim_one())
    return results
    
# results = sim_many(80000)
# np.mean(results) = 22182.855862500001
# np.std(results) == 2158.3301431052851
