import sys
import re

ifile = sys.argv[1]
D = open(ifile).read().strip()
# lines = D.split('\n')

ans = 0

# get each report
for i in range(len(D)):