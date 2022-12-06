import sys
lines = sys.stdin.readlines()

# Elf: A,B,C -> R,P,S
# Me: X,Y,Z -> R,P,S

ewin = ['AZ','BX','CY']
mwin = ['AY','BZ','CX']
draw = ['AX','BY','CZ']

totalPoints = 0

for l in lines:
    pts = 0
    ls = l.rstrip()
    play = ls.split()
    round = play[0] + play[1]
    myplay = play[1]

    # compair round to lists
    if round in ewin: winner = 'E'; pts = 0
    if round in mwin: winner = 'M'; pts = 6
    if round in draw: winner = 'D'; pts = 3

    # get my play choice/points
    if myplay == 'X': pts += 1
    if myplay == 'Y': pts += 2
    if myplay == 'Z': pts += 3
    
    totalPoints += pts

    print("E:" + play[0] + " --- M:" + play[1] + " --- R:" + round + " --- WINNER:" + winner + " --- MYPOINTS:" + str(pts)) 


print('Total Points: ' + str(totalPoints))

    