# cartesian coord math:

# start at (0,0)
moves = { 
    "U": (0,1), 
    "D": (0,-1), 
    "L": (-1,0), 
    "R": (1,0), 
    "UR": (1,1), 
    "DR": (1,-1),
    "UL": (-1,1),
    "DL": (-1,-1)
}

tailHist = {}

hcc = (0,0)
print(hcc)
print(moves)
for m in moves:
    print(moves[m])

hpos = ()   # current head coords
tpos = ()   # current tail coords

# coord equality...
hpos = (4,5)
tpos = (4,5)
print(f"hpos:{hpos} - tpos:{tpos}")
print(f"hpos == tpos? {hpos == tpos}")

print("hcc + U:")
# returns new coord after move(d)
def movePoint(p,d): 
    px, py = p
    dx, dy = moves[d]
    return(px+dx,py+dy)

hcc = movePoint(hcc,'U')
print(hcc)

print("hcc + L:")
hcc = movePoint(hcc,'L')
print(hcc)

print("hcc + L:")
hcc = movePoint(hcc,'L')
print(hcc)

print("hcc + R:")
hcc = movePoint(hcc,'R')
print(hcc)

print("hcc + D:")
hcc = movePoint(hcc,'D')
print(hcc)

hcc=(3,2)
print(f"hcc:{hcc}")
print("Adjacent 8 points to hcc:")

# list all ajacent points to hcc..
def adjacentPoints(hcc):
    for m in moves:
        mx,my = moves[m]
        hx,hy = hcc
        print(f"{m}:{(mx+hx,my+hy)}")

adjacentPoints(hcc)


hpos = (3,2)
tpos = (3,0)
# is the tail adjacent to head?
# overlapping is considered adjacent
def tailAdjacent() -> bool:
    for m in moves:
        mx,my = moves[m]
        hx,hy = hpos
        # print((mx+hx,my+hy))
        if ((mx+hx,my+hy) == tpos) or (hpos == tpos) :
            return True
    return False

print(f"hpos:{hpos} - tpos:{tpos}")
print(f"tpos ajacent to hpos? {tailAdjacent()}")

def pointDiff(): # hpos - tpos
    hx,hy = hpos
    tx,ty = tpos
    return(hx-tx,hy-ty)


# if we use this function, we know tailAdjacent failed.
def tailMove(): # moves
    global tpos, hpos 
    # do we need to move diagnally?
    if (hpos[0] != tpos[0]) and (hpos[1] != tpos[1]):
        print("moving tail diag...")
        px,py = pointDiff()
        # print(f"pointdiff:{(px,py)}")
        if (px > 0) and (py > 0):
            tpos = movePoint(tpos,'UR')
        elif (px < 0) and (py > 0):
            tpos = movePoint(tpos,'UL')
        elif (px < 0) and (py < 0):
            tpos = movePoint(tpos,'DL')
        elif (px > 0) and (py < 0):
            tpos = movePoint(tpos,'DR')

    # otherwise move UDLR
    else:
        print("moving tail linear...")
        # test for the direction to move;
        # hpos - tpos will give us a point with a 0(zero) and
        # a +- number in either position. the position and sign
        # of the number will tell us which way to move:
        #   (0,#)  - move tail +y (U)
        #   (0,-#) - move tail -y (D)
        #   (#,0)  - move tail +x (R)
        #   (-#,0) - move tail -x (L)

        # get diff - pointDiff() returns point to test
        px,py = pointDiff()

        if (px == 0) and (py > 0): 
            tpos = movePoint(tpos,'U')
        elif (px == 0) and (py < 0):
            tpos = movePoint(tpos,'D')
        elif (px > 0) and (py == 0):
            tpos = movePoint(tpos,'R')
        elif (px < 0) and (py == 0):
            tpos = movePoint(tpos,'L')
print("testing tailMove...\n")


tpos = (2,0)
print(f"hpos:{hpos} - tpos:{tpos}")
if not tailAdjacent():
    print("moving tail...")
    tailMove()
print(f"hpos:{hpos} - tpos:{tpos}\n")

tpos = (1,2)
print(f"hpos:{hpos} - tpos:{tpos}")
if not tailAdjacent():
    print("moving tail...")
    tailMove()
print(f"hpos:{hpos} - tpos:{tpos}\n")

tpos = (1,3)
print(f"hpos:{hpos} - tpos:{tpos}")
if not tailAdjacent():
    print("moving tail...")
    tailMove()
print(f"hpos:{hpos} - tpos:{tpos}\n")

tpos = (5,4)
print(f"hpos:{hpos} - tpos:{tpos}")
if not tailAdjacent():
    print("moving tail...")
    tailMove()
print(f"hpos:{hpos} - tpos:{tpos}\n")

print("test tailHist dictionary...")
tailHist[tpos] = None
print(tailHist)

tpos = (5,3)
tailHist[tpos] = None
print(tailHist)

tpos = (4,3)
tailHist[tpos] = None
print(tailHist)

tpos = (8,3)
tailHist[tpos] = None
print(tailHist)

print(f"tailHist len: {len(tailHist)}\n")


P1knots = [(3,2),(5,6)]
P2knots = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)] 
knots = P1knots
print(len(knots))
print(enumerate(knots))

for i in range(len(knots)-1):
    print(knots[i],knots[i+1])





        
        





