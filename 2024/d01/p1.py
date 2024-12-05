import sys

DATA = open(sys.argv[1]).read().strip()
lines = DATA.split('\n')

l1 = []
l2 = []
d1 = []
total = 0

for l in lines:
  loc1, loc2 = l.split()
  # print(f'{loc1} <> {loc2}')
  l1.append(int(loc1))
  l2.append(int(loc2))

l1.sort()
l2.sort()

for x in range(len(l1)):
  diff = abs(l1[x] - l2[x])
  d1.append(diff)

for j in d1:
  total += j

print(total)

