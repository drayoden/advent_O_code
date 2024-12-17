import sys
import re

ifile = sys.argv[1]
D = open(ifile).read().strip()
# lines = D.split('\n')

ans = 0

# get each report
for i in range(len(D)):
    if D[i:i+4] == 'mul(':
        j = i+4
        while D[j] != ')':
            j += 1

        try:
            x,y = map(int, re.findall('\d+', D[i:j+1]))
            if D[j-1] not in ['0','1','2','3','4','5','6','7','8','9']:
                continue
            ans += x*y
            print(D[i:j+1])
        except: 
            pass
print(ans)

