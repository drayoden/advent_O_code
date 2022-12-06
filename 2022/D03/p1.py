import sys
lines = sys.stdin.readlines()

pri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
typetotal = 0


for l in lines:
    line = l.rstrip()
    itype = ''

    # get length of string, split into equal halves
    halfline = int(len(line)/2)
    t1 = line[0:halfline:1]
    t2 = line[halfline::1]

    for c in t1:
        if c in t2: 
            itype = c
            break

    prival = pri.index(itype) + 1
    typetotal += prival

    print(line + ":  [" + t1 + "]:[" + t2 + "] --- type: " + itype + " --- val: " + str(prival))

print("priority value total: " + str(typetotal))


    