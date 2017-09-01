import itertools

# N is the number of players
N = 3

arrangements = list(itertools.product(['red', 'green'], repeat=N))

def strategy(info):
  """takes info about other players' hats and returns a guess"""
  if info.count('blue') == 0:
    return 'blue'
  elif info.count('red') == 0:
    return 'red'
  else:
    return None
  
for a in arrangements:
  guesses = []
  for p in range(N):
    
  
