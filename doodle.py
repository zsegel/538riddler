"""
Solution to July 27, 2018 Riddler Classic
(https://fivethirtyeight.com/features/the-perfect-doodle-puzzle-to-keep-you-busy-during-boring-meetings/)

        Start with an empty 5-by-5 grid of squares, and choose any square 
        you want as your starting square. The rules for moving through the 
        grid from there are strict:

        1. You may move exactly three cells horizontally or vertically, 
           or you may move exactly two cells diagonally.
        2. You are not allowed to visit any cell you already visited.
        3. You are not allowed to step outside the grid.

        You win if you are able to visit all 25 cells.

        Is it possible to win? If so, how? If not, what are the largest 
        and smallest numbers of squares you can legally visit?

SOLUTION: There are many ways to win.
Let's represent the 5 by 5 grid like this:

11 | 12 | 13 | 14 | 15
----------------------
21 | 22 | 23 | 24 | 25
----------------------
31 | 32 | 33 | 34 | 35
----------------------
41 | 42 | 43 | 44 | 45
----------------------
51 | 52 | 53 | 54 | 55

In the graph below, there are edges between each cell and every cell that's one move away from it.
The code just searches the graph randomly until it finds a simple path through the graph that's 25 cells long.
"""

graph = {
    11 : [14, 41, 33],
    12 : [15, 42, 34],
    13 : [43, 31, 35],
    14 : [11, 44, 32],
    15 : [12, 45, 33],
    21 : [24, 51, 43],
    22 : [25, 52, 44],
    23 : [53, 41, 45],
    24 : [21, 54, 42],
    25 : [22, 55, 43],
    31 : [34, 13, 53],
    32 : [14, 54, 35],
    33 : [11, 15, 51, 55],
    34 : [31, 12, 52],
    35 : [32, 13, 53],
    41 : [11, 44, 23],
    42 : [12, 45, 24],
    43 : [13, 21, 25],
    44 : [14, 41, 22],
    45 : [15, 42, 23],
    51 : [21, 54, 33],
    52 : [22, 55, 34],
    53 : [23, 31, 35],
    54 : [51, 24, 32],
    55 : [52, 25, 33]
}

import numpy as np

def random_path(graph):
    path = []
    current_node = np.random.choice(graph.keys())    # choose a starting node
    path.append(current_node)
    
    while [node for node in graph[current_node] if node not in path]:
        current_node = np.random.choice([node for node in graph[current_node] if node not in path])
        path.append(current_node)
    return path

def monte_carlo_path(graph, N):
    longest_path = []
    for i in range(N):
        path = random_path(graph)
        if len(path) == 25:
            return 25, path
        elif len(path) > len(longest_path):
            longest_path = path
    return len(longest_path), longest_path

print monte_carlo_path(graph, 5000)


"""
There are lots of solutions to this puzzle, e.g.:

[31, 53, 23, 41, 44, 22, 25, 43, 13, 35, 32, 14, 11, 33, 55, 52, 34, 12, 15, 45, 42, 24, 54, 51, 21]
[14, 44, 22, 52, 34, 31, 13, 43, 25, 55, 33, 11, 41, 23, 53, 35, 32, 54, 51, 21, 24, 42, 45, 15, 12]
[31, 34, 12, 42, 24, 21, 51, 54, 32, 14, 11, 41, 44, 22, 52, 55, 25, 43, 13, 35, 53, 23, 45, 15, 33]
[44, 22, 25, 43, 21, 24, 42, 45, 15, 12, 34, 52, 55, 33, 51, 54, 32, 14, 11, 41, 23, 53, 31, 13, 35]
[25, 22, 44, 14, 32, 35, 53, 23, 45, 15, 12, 42, 24, 54, 51, 21, 43, 13, 31, 34, 52, 55, 33, 11, 41]

etc.

zs
"""
