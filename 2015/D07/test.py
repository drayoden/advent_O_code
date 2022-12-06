
set = {}
set[0] = 'zero'
set[1] = 'one'
set[2] = 'two'
set[3] = 'three'

print(set)

def nonlooploop(x, t = {}, i = 0):
    if not x in t:
        c = set[x]
        t[i] = i + 7
        i += 1
    return t[x]

print(nonlooploop(2))