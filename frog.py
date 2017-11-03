"""
Solution to the Riddler Classic problem here:
https://fivethirtyeight.com/features/can-you-pick-up-sticks-can-you-help-a-frogger-out/

PROBLEM:

    A frog needs to jump across 20 lily pads. He starts on the shore (Number 0) and ends 
    precisely on the last lily pad (Number 20). He can jump one or two lily pads at a time. 
    How many different ways can he reach his destination?

    What if he can jump one, two or three at a time? Or four? Five? Six? Etc.

SOLUTION:  

    max jump: 2     ways to reach last lily pad:  10946
    
    max jump: 3     ways to reach last lily pad:  121415
    
    max jump: 4     ways to reach last lily pad:  283953
    
    max jump: 5     ways to reach last lily pad:  400096
    
    max jump: 6     ways to reach last lily pad:  463968
    
    max jump: 20    ways to reach last lily pad:  524288
"""

def count_jumps(max_jump, goal=20):
    jumps = range(1, max_jump+1)
    count = 0
    totals = [0]
    while totals: #while totals is non-empty
        total = totals.pop()
        if total < goal:
            totals.extend([total + j for j in jumps])
        elif total == goal:
            count += 1
    return count
