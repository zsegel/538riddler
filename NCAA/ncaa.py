"""
On Monday, Villanova won the NCAA men’s basketball national title. But I recently 
overheard some boisterous Butler fans calling themselves the “transitive national 
champions,” because Butler beat Villanova earlier in the season. Of course, other 
teams also beat Butler during the season and their fans could therefore make exactly 
the same claim.

How many transitive national champions were there this season? Or, maybe more 
descriptively, how many teams weren’t transitive national champions?
"""


# construct a directed graph with edges from each team to all the teams they lost to
graph = {}

f = open('ncaa.txt')
text = f.read().splitlines()

for line in text:
    line = line.replace('@', '') # remove @ symbols
    line = line.split()[1:] # remove first column (the date of the game)
    
    # extract team names and score from text and update graph
    team1 = ""
    team1_pts = 0
    team2 = ""
    team2_pts = 0
    
    index = 0
    while not team1_pts:
        try:
            team1_pts = int(line[index])
            index += 1
        except:
            team1 += line[index]
            index += 1
    while not team2_pts:
        try:
            team2_pts = int(line[index])
            index += 1
        except:
            team2 += line[index]
            index += 1
            
    if team1 not in graph:
        graph[team1] = []
    if team2 not in graph:
        graph[team2] = []
        
    if (team1_pts < team2_pts) and (team2 not in graph[team1]):
        graph[team1].append(team2)
    elif (team2_pts < team1_pts) and (team1 not in graph[team2]):
        graph[team2].append(team1)
        

# use depth-first search to find all teams that beat Villanova *transitively*
def dfs(graph, starting_node):
    """Returns the set of all nodes the starting_node can reach."""
    
    stack = [starting_node]
    visited = set()
    
    while stack:
        node = stack.pop()
        new_nodes = [n for n in graph[node] if n not in visited]
        stack.extend(new_nodes)
        visited = visited.union(set(new_nodes))
    return visited


all_teams = graph.keys()
transitive_champs = dfs(graph, 'Villanova')

print len(all_teams) - len(transitive_champs)

# Only about 13% of teams (177 out of 1362) do not count as transitive national champions.

