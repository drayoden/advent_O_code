import fileinput


sigcycles = [20,60,100,140,180,220]
crtrows = [40,80,120,160,200,240]
cyclevals = []

RegX = 1 # register starts with 1
RegXc = 0

# P2: CRT = 6 rows, 40 px each.
# current cycle determines the pixel 
# to be drawn. the pixel can only be drawn
# if one of the 3 pixel sprite is positioned
# (overlaps) the current pixel.
# - current pixel = cycle

cycle = 1
cmdi = 0
onecycle = True
CRT = ['.'] * 240   # 240 pixel CRT
sprite = (0,0,0)

COMMANDS = [l.strip() for l in fileinput.input() ]

def setSprite(x):
    return (x-1,x,x+1)

# test CRT:
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....

# breakpoint()
while True:
    

    sprite = setSprite(RegX + RegXc) # list of sprite pixels

    # P2 - need to determine if current pixel(cycle)
    # and the 3px sprite position(RegX) overlap here. 
    # If so set the CRT pixel -- CRT[cycle] = '*'
    if cycle-1 in sprite:
        CRT[cycle-1] = '*'

    print(f"c:{cycle} RegX:{RegX} sprite:{sprite}")
    if cycle in sigcycles:
        cyclevals.append(RegX * cycle)
    
    if onecycle: 
        sline = COMMANDS[cmdi].split()
        cmdi += 1
        if len(sline) == 2: # command
            print(f"CMD: addx {sline[1]}")
            cycleVal = int(sline[1])
            onecycle = not onecycle
        else:               # noop
            print("CMD: noop")
    else: 
        RegX += cycleVal
        onecycle = not onecycle
    
    if cmdi >= len(COMMANDS)-1: break 
    cycle += 1 

    # set RegXc per the value of cycle:
    for c in crtrows:
        if cycle > c:
            RegXc = c
    

print(f"cyclevals: {cyclevals}")
print(f"P1: -- sum of cyclevals: {sum(cyclevals)}")
print("P2: -- CRT:")
for i,px in enumerate(CRT):
    if (i%40) == 0: print()
    print(px,end='')
print("\n")


    



