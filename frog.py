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