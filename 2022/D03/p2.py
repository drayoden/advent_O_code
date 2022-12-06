import sys
lines = sys.stdin.readlines()

pri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
typetotal = 0

nlines = len(lines)
linesidx = 0

def proclist(l):
    e1 = l[0]
    e2 = l[1]
    e3 = l[2]

    for c in pri:
        if c in e1:
            if c in e2:
                if c in e3:
                    badge = c
                    break
    
    prival = pri.index(c) + 1
    print("E1:" + e1 + " E2:" + e2 + " E3:" + e3 + " BADGE:" + badge + " PRIVAL:" + str(prival))
    return prival

while True:
    if linesidx < nlines:
        list = []
        for i in range(3):
            list.append(lines[linesidx].rstrip())
            linesidx += 1
        typetotal += proclist(list)
    else: break

print("Priority total: " + str(typetotal))


    