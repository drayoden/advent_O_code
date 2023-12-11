import fileinput
import pprint as pp

LINES = [l.strip() for l in fileinput.input() ]

grid = list()
spos = [0,0,'a']
epos = [0,0,'z']
bpos = [0,0]
moves = list()

moves = { 
    "U": (-1,0), 
    "D": (1,0), 
    "L": (0,-1), 
    "R": (0,1), 
}

# get input, find me(S) and destination(E)
for l in LINES:
    grid.append([])
    for c in l:
        if c == 'S': spos[0] = LINES.index(l); spos[1] = l.index(c)
        if c == 'E': epos[0] = LINES.index(l); epos[1] = l.index(c)
        grid[LINES.index(l)].append(c)

print("grid:")
pp.pprint(grid)

moves = [['.']* len(grid[0])] * len(grid)

print("moves:")
pp.pprint(moves)
print()

print(f"grid[0][0]: {grid[0][0]}")
print(f"grid[1]: {grid[1]}")
print(f"grid[2][5]: {grid[2][5]}")
print(f"len(grid): {len(grid)} (rows)")
print(f"len(grid[0]): {len(grid[0])} (cols)")
print(f"S locaiton: {spos}, E location: {epos}")

# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^

# 5x8 = 40
# 8 (.) points not visited
# 40 - 8 = 32, 32 - 1 = 31 (end point is not counted)

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi

# bias:
# create/update (after each move) a bias list of two numbers (i,j). this list
# will 'bias' the next move. i or j can be 1,0 or -1. i is U<>D movement and
# j is L<>R movement based on my current location (r,c). the bias list can be
# calculated by comparing my (S) current location (r,c) to destination (E) location (r,c):
#   Er - Sr -> positive (E is below S)      -> i = 1
#           -> 0 (same row)                 -> i = 0
#           -> negative -> (E is above S)   -> i = -1 
#   Ec - Sc -> positive (E is right of S)   -> j = 1
#           -> 0 (same column)              -> j = 0
#           -> negative -> (E is left of S) -> j = -1
# a move will attempt to use ONE of the bias dirctions (cannot use both: diagnal not allowed)
# based on what UDLR moves are available. an available move bias to being hieher but can be equal
# in height (d = d) but cannot 'backtrack' thus each move will have, at most, three posibilites and
# will be determined by bias and height.
    
def getBias(s,e):
    Sr,Sc = s[0],s[1]
    Er,Ec = e[0],e[1]
    if (Er - Sr) > 0: Bi = 1
    if (Er - Sr) == 0:Bi = 0
    if (Er - Sr) < 0: Bi = -1
    if (Ec - Sc) > 0: Bj = 1
    if (Ec - Sc) == 0:Bj = 0
    if (Ec - Sc) < 1: Bj = -1
    return Bi,Bj

bias = getBias(spos,epos)
print(f"bias:{bias}")

print(f"a < z: {'a' < 'z'}")
print(f"h > z: {'h' > 'z'}")
print(f"d == d: {'d' == 'd'}")
# print(f"a - a: {ord('a') - ord('a')}")
# print(f"d - c: {ord('d') - ord('c')}")
# print(ord('a'),ord('z'))
    

# possible moves for S:
# using bias -> spos + bias(one at a time):

for b in bias:
    if b != 0:
        bpos[bias.index(b)] = 1
    else: 
        bpos[bias.index(b)] = 0

print(bpos)


# compare height at bpos[0] with spos:
# print(grid[bpos[0][0]][bpos[0][1]],spos[2])
# if ( ord(grid[bpos[0][0]][bpos[0][1]])) == ord(spos[2]):
#     print(f"bpos[0] equal to spos")
# if ( ord(grid[bpos[1][0]][bpos[1][1]])) == ord(spos[2]):
#     print(f"bpos[1] equal to spos")








