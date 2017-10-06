import itertools

boxes = [1, 2, 3, 4]
names = ['A', 'B', 'C', 'D']

name_orders = list(itertools.permutations(names))
individual_strategies = list(itertools.combinations(boxes, 2))
all_strategies = list(itertools.product(individual_strategies, repeat=4))

def eval_strategy(s):
    wins = 0
    for order in name_orders:
        wins +=
(np.sum([order.index(names[i]) in s[i] for i in range(4)]) == 4)
                                   
                                   
                                   
