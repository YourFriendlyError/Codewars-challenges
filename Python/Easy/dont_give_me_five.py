def dont_give_me_five(start, end):
    n = 0
    for i in range(start, end+1):
        num = str(i)
        if num.__contains__('5'):
            continue
        else:
            n += 1
    return n