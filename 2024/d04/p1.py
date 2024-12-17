import sys
import re

ifile = sys.argv[1]
D = open(ifile).read().strip()

Grid = D.split('\n')
R = len(Grid)
C = len(Grid[0])
ans = 0

for r in range(R):
    for c in range(C):
        # FORWARD
        if c+3<C and Grid[r][c] =='X' and Grid[r][c+1] == 'M' and Grid[r][c+2] == 'A' and Grid[r][c+3] == 'S':
            ans += 1 
        # BACKWARD
        if c+3<C and Grid[r][c+3] =='X' and Grid[r][c+2] == 'M' and Grid[r][c+1] == 'A' and Grid[r][c] == 'S':
            ans += 1 
        

print(ans)







