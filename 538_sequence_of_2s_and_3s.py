'''
Solution to the Riddler Classic problem found here:

'''

# We can use the first four entries in the sequence to generate as many more as we please.
sequence = [3, 3, 3, 2]

# Let's apply the sequence-generating rules 10,000,000 times:
iterations = 10000000
for i in range(1, iterations):
    if sequence[i] == 3:
        sequence.extend([3, 3, 3, 2])
    else:
        sequence.extend([3, 3, 2])

# Now we just have to count the number of twos and threes in the list...
twos = sequence.count(2)
threes = len(sequence) - twos

# And calculate the ratio of threes to twos:
print float(threes) / twos


'''
As the length of the sequence approaches infinity, the ratio of threes to twos in the 
sequence approaches sqrt(3) + 1. There might be an interesting reason why this is the 
case, but I don't know what that reason is. 
'''