import sys

# kudos to Jonathan Paulson (YT)

ifile = sys.argv[1]
D = open(ifile).read().strip()
lines = D.split('\n')

ans = 0

# get each report
for line in lines:
    r1 = list(map(int, line.split()))
    good = False

    for j in range(len(r1)):
        # build new report with one extracted level
        r = r1[:j] + r1[j+1:]

        # use sort to determine if list is sorted Inc, or Dec
        IorD = (r==sorted(r) or r==sorted(r,reverse=True))
        
        safe = True

        # is diff of each pair within range?
        for x in range(len(r)-1):
            diff = abs(r[x] - r[x+1])
            if not 1 <= diff <= 3:
                safe = False
        if safe and IorD:
            good = True
    if good:
        ans += 1

print(ans)
