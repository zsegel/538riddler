import numpy as np

"""
11 | 12 | 13 | 14 | 15
----------------------
21 | 22 | 23 | 24 | 25
----------------------
31 | 32 | 33 | 34 | 35
----------------------
41 | 42 | 43 | 44 | 45
----------------------
51 | 52 | 53 | 54 | 55
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

def random_path(graph):
    nodes = graph.keys()
    path = []
    
    current_node = np.random.choice(nodes)
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
