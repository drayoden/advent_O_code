import sys, re
from collections import defaultdict
DATA = open(sys.argv[1]).read().strip()     # one big string
print(DATA)
lines = DATA.split('\n')                    # list of strings
GRID = [[c for c in line] for line in lines]    # list of list of chr
R = len(GRID)
C = len(GRID[0])
total1 = 0
total2 = 0

nums = defaultdict(list)
# print(type(nums))

for r in range(len(GRID)):  # get rows
    # rownums = re.findall('-?\d+', lines[r])
    # print(rownums)
    gears = set()
    n = 0
    part = False
    # print(f'[{r}][{len(GRID[r])}] {"-"*50}')
    for c in range(len(GRID[r])+1):  #get cols
        if c < C and GRID[r][c].isdigit():
            n = n*10 + int(GRID[r][c])
            
            # test all directions from current digit
            for rr in [-1,0,1]:
                for cc in [-1,0,1]:
                    if 0 <= r + rr < R and 0 <= c + cc < C:
                        ch = GRID[r+rr][c+cc]
                        if not ch.isdigit() and ch != '.':
                            part = True
                        if ch == '*':
                            gears.add((r+rr,c+cc))  # key index of '*'
        elif n > 0:
            for gear in gears:
                nums[gear].append(n) # value list
            print(n, part)
            if part:
                total1 += n
            n = 0
            part = False
            gears = set()


print(f'part1: {total1}')
# print(nums)
for k,v in nums.items():
    # print(k,v)
    if len(v) == 2:
        total2 += v[0]*v[1]
print(f'part2: {total2}')


# a1: 543410 low
# a1: 546312 huzzah! 
# a2: 


