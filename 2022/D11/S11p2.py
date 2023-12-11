import fileinput, os, math, copy
import re, pprint as pp

LINES = "".join(fileinput.input())
monkeys = {}  # dict
rounds = 10000


# Part 2 was really hard for me. Each item (int) became VERY large VERY fast
# and very quickly brought everything to a crawl.
# I started looking at solutions from others doing AoC and found the answer. After 
# studying this answer for quite a while (very nice concise soltuion!):
# https://github.com/jmerle/advent-of-code-2022/tree/master/src/day11
# I realized I had seen this "item = item % mod" before but was not sure the purpose.
# I did some digging regarding the modulo operator and found it can be use to constrain
# numbers to a max value (no bitints):
mod = 1     

# build the monkey dictionary...
for monkey in LINES.split(os.linesep * 2):  # divides monkeys between '\r\n'
    m = monkey.splitlines() # divides the lines of each monkey
    id = int(re.findall(r'[0-9]+',m[0])[0])
    items = re.findall(r'[0-9]+',m[1])  # creates a list of strings
    items = [int(x) for x in items]     # changes to list of ints
    opr = m[2].split("old")[1]
    div = int(re.findall(r'[0-9]+',m[3])[0])
    true = int(re.findall(r'[0-9]+',m[4])[0])
    false = int(re.findall(r'[0-9]+',m[5])[0])
    monkeys[id] = items,opr,div,true,false
    mod *= div

print("BEFORE monkey business starts:")
pp.pprint(monkeys)
insp = ([0]*len(monkeys))   # create a list of inspected items for each monkey

for i in range(1, rounds+1, 1):
    print(f" --- Round:{i} ---")
    for m in monkeys:
        tmonkeys = copy.deepcopy(monkeys[m][0]) # make a copy of items
        for i in tmonkeys: # items
            # print(f"Monkey:{m} item:{i}")
            insp[m] += 1
            opr = monkeys[m][1].split() # opr
            if len(opr) == 1:
                wlevel = pow(i,2)
            elif opr[0] == "*":
                wlevel = i * int(opr[1])
            else: wlevel = i + int(opr[1])
            wlevel = wlevel % mod 
            wlevel = math.floor(wlevel)
            # print(wlevel)
            if (wlevel % monkeys[m][2]) == 0: # div
                monkeys[monkeys[m][3]][0].append(wlevel) # true
            else:
                monkeys[monkeys[m][4]][0].append(wlevel) # false
            monkeys[m][0].pop(0)

print("POST monkey business:")
pp.pprint(monkeys)
print(insp)
insp.sort(reverse=True)
print(f"Monkey business level: {insp[0] * insp[1]}")

