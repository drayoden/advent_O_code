import sys

total = 0
twodig = False   # this is LAME, just getting warmed up...

for line in sys.stdin:
    ls = line.rstrip()
    numtxt = list("xx")
    for c in ls:
        if c.isnumeric():
            if twodig:
                numtxt[1] = c
            else:
                numtxt[0] = c
                numtxt[1] = c
                twodig = True  
    twodig = False
    print(f'numtxt: {numtxt}')
    print(f'join(numtxt): {"".join(numtxt)}')
    total += int("".join(numtxt))

print(f'Total: {total}')
            

        

