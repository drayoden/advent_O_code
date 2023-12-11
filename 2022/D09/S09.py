import fileinput

# P2 - need to refactor funcitons to take args: tail,head

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

tailHist = {}   # all unique positions of tail

# head is always knots[0] tail is always knots[n]
P1knots = [(0,0),(0,0)]
P2knots = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)] 
knots = P2knots

# returns new coord after moving point(p) in direction(d)
def movePoint(p,d): 
    px, py = p
    dx, dy = moves[d]
    return(px+dx,py+dy)

# is the tail adjacent to head?
# overlapping is considered adjacent
def tailAdjacent(h,t) -> bool:
    for m in moves:
        mx,my = moves[m]
        hx,hy = h
        # print((mx+hx,my+hy))
        if ((mx+hx,my+hy) == t) or (h == t) :
            return True
    return False

def pointDiff(h,t): # head - tail
    hx,hy = h
    tx,ty = t
    return(hx-tx,hy-ty)

def tailMove(h,ti): # moves tail(s)
    
    px,py = pointDiff(h,knots[ti])

    # do we need to move diagnally?
    if (h[0] != knots[ti][0]) and (h[1] != knots[ti][1]):
        print("moving tail diag...")
        # print(f"pointdiff:{(px,py)}")
        if (px > 0) and (py > 0):
            knots[ti] = movePoint(knots[ti],'UR')
        elif (px < 0) and (py > 0):
            knots[ti] = movePoint(knots[ti],'UL')
        elif (px < 0) and (py < 0):
            knots[ti] = movePoint(knots[ti],'DL')
        elif (px > 0) and (py < 0):
            knots[ti] = movePoint(knots[ti],'DR')

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
        if (px == 0) and (py > 0): 
            knots[ti] = movePoint(knots[ti],'U')
        elif (px == 0) and (py < 0):
            knots[ti] = movePoint(knots[ti],'D')
        elif (px > 0) and (py == 0):
            knots[ti] = movePoint(knots[ti],'R')
        elif (px < 0) and (py == 0):
            knots[ti] = movePoint(knots[ti],'L')


COMMANDS = [l.strip() for l in fileinput.input() ]

for cmd in COMMANDS:
    DIR = cmd.split()[0]
    STP = int(cmd.split()[1])
    print(DIR,STP)

    # loop STP times: 
    #   move head, update knots[0]
    #   move tail
    for i in range(1, STP+1, 1):
        print("move head...")
        knots[0] = movePoint(knots[0],DIR)
        print("move tail...")
        for i in range(len(knots)-1):
            if not tailAdjacent(knots[i],knots[i+1]):
                tailMove(knots[i],i+1)
        tailHist[knots[len(knots)-1]] = None # update tail
    

print()
print(f"hpos:({knots[0]})")
print(f"tpos:({knots[len(knots)-1]})")
print(f"no of knots: {len(knots)}")
print(f"total tail positions: {len(tailHist)}")


