import fileinput


EXT = [
    (0,1),
    (0,-1),
    (-1,0),
    (1,0)
]

# this creates a dictionary of '(x,y): c'
grid = {}
for y, line in enumerate(fileinput.input()):
    for x, c in enumerate(line.strip()):
        grid[x, y] = int(c)

print(grid)

for tree in grid:
    print(tree)


for dx,dy in EXT:
    print(dx,dy)

