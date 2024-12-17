import sys
import re

ifile = sys.argv[1]
D = open(ifile).read().strip()
# lines = D.split('\n')

ans = 0
go = True
# get each report
for i in range(len(D)):
    if D[i:i+4] == 'do()':
        go = True
    if D[i:i+7] == "don't()":
        go = False
    if D[i:i+4] == 'mul(':
        j = i+4
        while D[j] != ')':
            j += 1

        try:
            x,y = map(int, re.findall('\d+', D[i:j+1]))
            if D[j-1] not in ['0','1','2','3','4','5','6','7','8','9']:
                continue
            if go:
                ans += x*y
                print(D[i:j+1])
        except: 
            pass
print(ans)

# low: 71719142


