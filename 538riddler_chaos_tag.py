# On a sunny summer day, you’ve gone to the park with your friends. 
# After the picnic is eaten, you decide to enjoy the weather by playing 
# a nice game of chaos tag. For those uninitiated in the joys of chaos 
# tag, you explain the following rules:

# 1. Any group of two or more people can play. 
#    All players are active at the start of the game.
# 2. Active players can run around and tag other active players.
# 3. A player who is tagged becomes inactive and must sit on the spot where they were tagged.
# 4. An inactive player becomes active again when the player who tagged them is tagged.
# 5. Victory is achieved by being the only remaining active player.

# Suppose N of you are at the park that day. 
# If all active players are equally likely to 
# tag someone and any of the possible targets 
# are equally likely to be tagged, how long will 
# the game last on average, as measured in tags? 

# (For example, with two players, the game always ends in one tag; 
# with three players, the expected length of the game is three tags.)






#MODELING THE GAME

import numpy as np
import random

class Field(object):
    def __init__(self, players):
        self.players = players
        self.active_players = players #all players are active at the start of the game
        self.inactive_players = []
        self.tag_count = 0
        
    def update_active_and_inactive_players(self):
        self.active_players = [p for p in self.players if p.is_active]
        self.inactive_players = [p for p in self.players if p not in self.active_players]
    
    def one_tag(self):
        #update the tag count
        self.tag_count += 1
        
        #copy the potential taggers and taggees into a list
        potential_taggers_and_taggees = [p for p in self.players if p in self.active_players]
        
        #pick the tagger
        tagger = random.choice(potential_taggers_and_taggees)
        potential_taggers_and_taggees.remove(tagger)
        
        #pick the taggee
        taggee = random.choice(potential_taggers_and_taggees)
        
        #the tagger tags the taggee
        tagger.tag(taggee)
        
        self.update_active_and_inactive_players()

        #any inactive player who was tagged by the taggee becomes active
        for p in self.inactive_players:
            if taggee.number == p.tagged_by:
                p.is_active = True
                p.tagged_by = 'n/a'
                
        self.update_active_and_inactive_players()
        
    def game_over(self):
        #checks whether the game is over
        if len(self.active_players) > 1:
            return False
        else:
            return True

    def play_a_game(self):
        while not self.game_over():
            self.one_tag()
        else:
            return self.tag_count
         
        
class Player(object):
    def __init__(self, number):
        self.number = number
        self.is_active = True
        self.tagged_by = 'n/a'
    
    def tag(self, player):
        #tags another player
        player.is_active = False
        player.tagged_by = self.number
        
        
        
def create_players(n):
    players = []
    for i in range(n):
        players.append(Player(i))
    return players

def create_field(n):
    field = Field(create_players(n))
    return field

def simulate_tag(players, simulations):
    results = []
    for i in range(simulations):
        field = create_field(players)
        results.append(field.play_a_game())
    return results




#SIMULATING THE GAME REPEATEDLY (FOR DIFFERENT VALUES OF N)

xs = np.arange(2, 9)
ys = []

for x in xs:
    y = np.mean(simulate_tag(x, 5000))
    print "# of players:", x, "-------> estimated avg. # of tags:", y
    ys.append(y)


#RESULTS

# when players = {2, 3, 4, 5, 6, 7, 8, ...},
# the game lasts {1, 3, 7, 15, 31, 63, 127, ...} rounds

# in general, when there are N players, the game lasts (2^(N-1) - 1) rounds, on average
