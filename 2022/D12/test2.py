import fileinput
import pprint as pp
from collections import deque

grid = {} # dictionary
LINES = [l.strip() for l in fileinput.input() ]

for y,l in enumerate(LINES):
    for x,c in enumerate(l):
        grid[(x,y)] = c
        if c == 'S':
            start = (x,y)
            grid[start] = 'a'
        if c == 'E':
            end = (x,y)
            grid[end] = 'z'
            

pp.pprint(grid)
print(f"start:{start}")
print(f"end:{end}")

x = deque([start,0])
print(x)
p,depth = x.popleft()
print(p,depth)
print(x)
x.popleft()
print(x)
















