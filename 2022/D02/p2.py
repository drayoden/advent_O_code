import sys
lines = sys.stdin.readlines()

# Elf: A,B,C -> R,P,S
# Me: X,Y,Z -> R,P,S

# Col2: X = lose, Y = draw, Z = win

ewin = ['AZ','BX','CY']
mwin = ['AY','BZ','CX']
draw = ['AX','BY','CZ']

totalPoints = 0

for l in lines:
    pts = 0
    ls = l.rstrip()
    play = ls.split()
    round = play[0] + play[1]
    wld = play[1]
    eplay = play[0]

    # get the correct list
    if wld == 'X': 
        winner = 'E'
        pts = 0

    if wld == 'Y': 
        winner = 'D'
        pts = 3

    if wld == 'Z': 
        winner = 'M'
        pts = 6

    # get my play choice/points
    if winner == 'E':
        l = ['Z','X','Y']
        for i, p in enumerate(ewin):
            if eplay + l[i] == p:
                myplay = l[i]
                break

    if winner == 'D':
        l = ['X','Y','Z']
        for i, p in enumerate(draw):
            if eplay + l[i] == p:
                myplay = l[i]
                break

    if winner == 'M':
        l = ['Y','Z','X']
        for i, p in enumerate(mwin):
            if eplay + l[i] == p:
                myplay = l[i]
                break

    
    if myplay == 'X': pts += 1
    if myplay == 'Y': pts += 2
    if myplay == 'Z': pts += 3
    
    totalPoints += pts

    print("E:" + play[0] + " --- M:" + play[1] + " --- R:" + round + " --- WINNER:" + winner + " --- MYPOINTS:" + str(pts)) 


print('Total Points: ' + str(totalPoints))

    