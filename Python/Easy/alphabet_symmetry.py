def solve(words: list):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    counted = []
    pos = 0
    for select in words:
        print('\n')
        for k, letter in enumerate(select):
            if k == alpha.find(letter.lower()): # Compare the 'k' number to the position of the 'alpha' list
                count += 1
                #print('{} = {} : counted = {}'.format(letter, k+1, count))
        counted.insert(pos, count)
        count = 0
        pos += 1
    return counted