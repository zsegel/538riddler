n = 5
while True:
    cpn = (5*n**2 + 5*n + 2)/2 # generate next centered pentagonal number
    
    x = ((cpn-1)/2)**0.5       # test whether one less than that number
    if x == int(x):            # is a twice a perfect square
        break
    else:
        n += 1
print(int(cpn-1))