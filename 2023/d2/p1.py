import sys, math
lines = sys.stdin.readlines()
gnsum = 0
powers = 0

for l in lines:
    sline = l.rstrip()
    game,sets = sline.split(':')
    (_,gn) = game.split()
    accept = True
    rgb = [1,1,1]
    for cubeset in sets.split(';'):
        for cubes in cubeset.split(','):
            n,color = cubes.split()
            if int(n) > {"red":12,"green":13,"blue":14}.get(color,0):
                accept = False
            clri = ["red","green","blue"].index(color)
            if int(n) > rgb[clri]:
                rgb[clri] =int(n)
    powers += math.prod(rgb)
    if accept:
        print(f'*{sline}')
        gnsum += int(gn)
    else:
        print(f'{sline}')
    

print(gnsum)
print(powers)