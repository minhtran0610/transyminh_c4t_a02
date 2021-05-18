def steps(source, step, dest):
    #base cases
    if (abs(source) > abs(dest)):
        return abs(dest) * 2 -1

    if (source == dest):
        return step
    
    # at each point we can go either way
    # if we go on positive side
    pos = steps(source + step +1, step + 1, dest)

    # if we go on negative side
    neg = steps(source - step - 1, step + 1, dest)

    # minimum of both cases
    return min(pos, neg)

