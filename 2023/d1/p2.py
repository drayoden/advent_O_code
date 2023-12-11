import sys

total = 0
txtnums = ('one','two','three','four','five','six','seven','eight','nine')
dignums = ('1','2','3','4','5','6','7','8','9')

def padlist(rlst,llen):
    return rlst + [0]*(llen - len(rlst))

for line in sys.stdin:
    sline = line.rstrip()   # stripped line (no cr/lf)
    ilst = []


    # iterate both lists (txtnums,dignums)
    print(sline)
    ilist = []
    for i, tnum in enumerate(txtnums):
        
        # first text number 
        try:
            x = sline.index(tnum)
            if len(ilist) < x+1:
                ilist = padlist(ilist,x+1)
            ilist[x] = i+1 
        except: pass

        # last text number
        try:
            x = sline.rindex(tnum)
            if len(ilist) < x+1:
                ilist = padlist(ilist,x+1)
            ilist[x] = i+1 
        except: pass

        # first digit number
        try: 
            x = sline.index(dignums[i])
            if len(ilist) < x+1:
                ilist = padlist(ilist,x+1)
            ilist[x] = i+1
        except: pass

        # last digit number
        try: 
            x = sline.rindex(dignums[i])
            if len(ilist) < x+1:
                ilist = padlist(ilist,x+1)
            ilist[x] = i+1
        except: pass

        # print(f'{tnum}[{dignums[i]}] - ilist: {ilist}')        
    for j in ilist:
        if not j == 0:
            firstnum = j
            break
    lastnum = ilist[len(ilist) -1]
    num = int(str(firstnum) + str(lastnum))
    total += num

    print(f'num: {num}')





print(f'Total: {total}')
            

        

