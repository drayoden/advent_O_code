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
            # print("forward...")
            ans += 1
        # BACKWARD
        if c+3<C and Grid[r][c+3] =='X' and Grid[r][c+2] == 'M' and Grid[r][c+1] == 'A' and Grid[r][c] == 'S':
            # print("backward...")
            ans += 1
        # UP
        if r-3>0 and Grid[r][c] =='X' and Grid[r-1][c] == 'M' and Grid[r-2][c] == 'A' and Grid[r-3][c] == 'S':
            # print("up...")
            ans += 1
        # DOWN
        if r+3<R and Grid[r][c] =='X' and Grid[r+1][c] == 'M' and Grid[r+2][c] == 'A' and Grid[r+3][c] == 'S':
            # print("down...")
            ans += 1
        # DIAG UR
        if r-3>0 and c+3<C and Grid[r][c] =='X' and Grid[r-1][c+1] == 'M' and Grid[r-2][c+2] == 'A' and Grid[r-3][c+3] == 'S':
            # print("diagUR...")
            ans += 1
        # DIAG UL
        if r-3>0 and c+3<C and Grid[r][c] =='X' and Grid[r-1][c-1] == 'M' and Grid[r-2][c-2] == 'A' and Grid[r-3][c-3] == 'S':
            # print("diagUL...")
            ans += 1
        # DIAG DR
        if r+3<R and c+3<C and Grid[r][c] =='X' and Grid[r+1][c+1] == 'M' and Grid[r+2][c+2] == 'A' and Grid[r+3][c+3] == 'S':
            # print("diagDR...")
            ans += 1
        # DIAG DL
        if r+3<R and c-3>0 and Grid[r][c] =='X' and Grid[r+1][c-1] == 'M' and Grid[r+2][c-2] == 'A' and Grid[r+3][c-3] == 'S':
            # print("diagDL...")
            ans += 1



print(ans)

# 2413: low
#
