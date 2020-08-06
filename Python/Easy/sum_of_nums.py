def get_sum(a,b):
    if a == b:
        return a
    else:
        s = 0
        for n in range(min(a,b), max(a,b)+1):
            s += n
        return s