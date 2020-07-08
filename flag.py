"""
Riddler Classic (3 July 2020)
It just so happens that when N equals 50, N is twice a square and N+1 is a centered 
pentagonal number. After 50, what is the next integer N with these properties?
"""
n = 5
while True:
    cpn = (5*n**2 + 5*n + 2)/2 # generate next centered pentagonal number
    
    x = ((cpn-1)/2)**0.5       # test whether one less than that number
    if x == int(x):            # is a twice a perfect square
        break
    else:
        n += 1
print(int(cpn-1))
# Answer: 16200
