import sys

ifile = sys.argv[1]
D = open(ifile).read().strip()
lines = D.split('\n')

ans = 0

# get each report
for line in lines:
    r = list(map(int, line.split()))