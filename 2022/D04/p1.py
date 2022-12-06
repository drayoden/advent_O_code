import sys
lines = sys.stdin.readlines()
contain = 0

# find all totally contained pairs

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

    # E1 in E2
    if (e1s >= e2s) and (e1e <= e2e):
        contain += 1
        info += "E1 in E2"
    # E2 in E1
    elif (e2s >= e1s) and (e2e <= e1e):
        contain += 1
        info += "E2 in E1"
    else:
        info += "Not Contain..."

    print(info)

print("Total containment pairs: " + str(contain))





