import sys
lines = sys.stdin.readlines()
contain = 0

# find any overlaping pairs

for l in lines:
    line = l.rstrip()
    secs = line.split(',')
    e1 = secs[0].split('-')
    e2 = secs[1].split('-')

    info = "E1:[" + secs[0] + "] E2:[" + secs[1] + "] "

    e1s = int(e1[0])
    e1e = int(e1[1])
    e2s = int(e2[0])
    e2e = int(e2[1])

    # E1 overlaps E2
    if (e2s <= e1s <= e2e) or (e2s <= e1e <= e2e):
        contain += 1
        info += "overlap"
    # E2 overlaps E1
    elif (e1s <= e2s <= e1e) or (e1s <= e2e <= e1e) :
        contain += 1
        info += "overlap"
    else:
        info += "No overlap"

    print(info)

print("Total overlap pairs: " + str(contain))





