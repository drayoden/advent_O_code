import sys
import pprint

import sys

with open(sys.argv[1],'r') as f:
    lines = f.readlines()

pp = pprint.PrettyPrinter(width=70, compact=True)
# lines = sys.stdin.readlines()
visibletrees = 0 

dim = len(lines)    # grid is square

print(f"Tree grid is {dim}x{dim}")

# initalize treegrid...
tgrid =[]
for r in range(0, dim, 1):
    tgrid.append([])
    for c in range(0, dim, 1):
        tgrid[r].append([0,False])

print("Initialize empty tree grid...")
# pp.pprint(tgrid)
# print()

print("Loading tree grid into array...")
for r, l in  enumerate(lines):
    line = l.rstrip()
    for c,t in enumerate(line):  # get each 'tree' and build a list: (int,bool)
        tgrid[r][c] = [int(t),False]


# pp.pprint(tgrid)
# print()

# make all edge trees visible(True)
for r in range(0, dim, 1):
    for c in range(0, dim, 1):
        if r == 0 or c == 0 or r == dim-1 or c == dim-1:
            tgrid[r][c][1] = True

# pp.pprint(tgrid)
# print()

for r in range(0, dim, 1):
    for c in range(0, dim, 1):
        if tgrid[r][c][1] == True:
            visibletrees += 1


print(f"All border trees are visible: {visibletrees}... ")

# !!! -- trees can be visible from any direction(NSEW)
# test the value(h) at r,c:
def testtree(r,c,h):
    # breakpoint()
    ltemp = []
    # print(f"rch:{r,c,h}")
    # check all trees in the same row - column changes...
    for col in range(0, dim, 1):
        # print(f"col:{col}:{dim}") 
        if (col < c) or (col > c):
            ltemp.append(tgrid[r][col][0])
            # print(ltemp)
        if (col == c) or (col == dim-1):
            if ltemp:
                if (h > max(ltemp)):
                    return True
                ltemp = []
        
    ltemp = []
    # check all trees in the same column - row changes...
    for row in range(0, dim, 1):
        if (row < r) or (row > r):
            ltemp.append(tgrid[row][c][0])
            # print(ltemp)
        if (row == r) or (row == dim-1):
            if ltemp:
                if (h > max(ltemp)):
                    return True
            ltemp = []  

    return False
    
    

# only iterate over the inner trees...
for r in range(1, dim-1, 1):
    for c in range(1, dim-1, 1):
        if testtree(r,c,tgrid[r][c][0]):
            tgrid[r][c][1] = True

# print("Populated tree grid...")
# pp.pprint(tgrid)
# print()

visibletrees = 0

for r in range(0, dim, 1):
    for c in range(0, dim, 1):
        if tgrid[r][c][1] == True:
            visibletrees += 1

print(f"P1: - Total visible trees: {visibletrees}")


print(f"Initialize all trees with scenic score = 0")
for r in range(0, dim, 1):
    for c in range(0, dim, 1):
        tgrid[r][c][1] = 0

# pp.pprint(tgrid)

def setScore(r,c) -> int:

    scores = [] # four scores from N,S,E,W below...
    fscore = 1
    # print(f"****{r,c,tgrid[r][c][0]}")

    # count number of trees in direction(N,S,E,W) until 
    # you find a tree of equal or greater height.

    # go North(up) 
    # print("->N")
    for i,row in enumerate(range(r-1,-1,-1)):
        # print(row,c,tgrid[row][c][0],i)
        if (tgrid[row][c][0] >= tgrid[r][c][0]) or (row == 0):
            scores.append(i+1)
            break
    # print(f"scores:{scores}")
    
    # go South(down)
    # print("->S")
    for i,row in enumerate(range(r+1,dim,1)):
        # print(row,c,tgrid[row][c][0],i)
        if (tgrid[row][c][0] >= tgrid[r][c][0]) or (row == dim-1):
            scores.append(i+1)
            break
    # print(f"scores:{scores}")

    # go East(left)
    # print("->E")
    for i,col in enumerate(range(c+1,dim,1)):
        # print(r,col,tgrid[r][col][0],i)
        if (tgrid[r][col][0] >= tgrid[r][c][0]) or (col == dim-1):
            scores.append(i+1)
            break
    # print(f"scores:{scores}")

    # go West(right)
    # print("->W")
    for i,col in enumerate(range(c-1,-1,-1)):
        # print(r,col,tgrid[r][col][0],i)
        if (tgrid[r][col][0] >= tgrid[r][c][0]) or (col == 0):
            scores.append(i+1)
            break
    # print(f"scores:{scores}")

    for s in scores:
        fscore *= s
    return fscore

print("Set scenic score for all trees...")
# only iterate over the inner trees...
for r in range(1, dim-1, 1):
    for c in range(1, dim-1, 1):
         tgrid[r][c][1] = setScore(r,c)


# find the tree with the highest scenic score,
# only search the inner trees...
highScenicScore = 0
for r in range(1, dim-1, 1):
    for c in range(1, dim-1, 1):
         if tgrid[r][c][1] > highScenicScore: highScenicScore = tgrid[r][c][1]

print(f"P2: - highest scenic score: {highScenicScore} ")

















        





