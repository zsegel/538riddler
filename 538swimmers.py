import numpy as np


def find_angle(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    if x == 0:
        x += 0.00001
    return np.arctan2(float(y), float(x))

def distance(a, b):
    return round(np.sqrt((a[1]-b[1])**2 + (a[0]-b[0])**2), 2)  


class Swimmer(object):
    
    def __init__(self, name, speed, initial_position, initial_direction):
        self.name = name
        self.speed = speed
        self.position = initial_position
        self.direction = initial_direction
        self.time = 0
        
    def __repr__(self):
        return self.name
    
    def update_position(self, time):
        vx = self.speed * np.cos(self.direction)
        vy = self.speed * np.sin(self.direction)
        self.position[0] += time * vx
        self.position[1] += time * vy
        self.time += time
        
    def update_direction(self, anchor_position):
        self.direction = find_angle(self.position, anchor_position)


t = 0.001 #time increment
speed = 10

swimmerA = Swimmer('Swimmer A', speed, [100, 0], 1.5707963267948966)
swimmerB = Swimmer('Swimmer B', speed, [0,0], 0)

d = []

for i in range(50000):

    swimmerA.update_position(t)
    swimmerB.update_position(t)
    
    swimmerB.update_direction(swimmerA.position)
    
    d.append(distance(swimmerA.position, swimmerB.position))
    
print distance(swimmerA.position, swimmerB.position)