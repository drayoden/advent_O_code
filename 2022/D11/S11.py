import fileinput
import math
import copy

### input example ###
# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# P1 complete! However, this is not going
# to work for part2. It took over 20min to 
# do the test to 20 rounds! Need to refactor this
# internal numbers get REALLY big REALLY fast!
# I think the use of an object (class) was
# slowing things down. 

class Monkey:
    def __init__(self,id: int, insp = 0):
        self.id = id
        self.items = []
        self.insp = insp
        self.opr = str
        self.test = int
        self.testT = int
        self.testF = int
    
    def __str__(self):
        return f"id:{self.id} items:{self.items} opr:{self.opr} test:{self.test} testT:{self.testT} testF:{self.testF}"

PART = "P1"

rounds = 20
divisor = 3

tmpM = Monkey

monkeys = {} # dict of monkeys

iline = 0 # input index

LINES = [l.strip() for l in fileinput.input() ]

print("Get input...")
# get input to build a collection of monkeys:
while True:
    items = []
    if LINES[iline]:
        sline = LINES[iline].split()
        if (sline[0] == "Monkey"):
            id = int(sline[1][0])                   # id
            iline += 1
            sline = LINES[iline].split(':')
            sitems = sline[1].split(",")
            for i in sitems:
                items.append(int(i))                # items
            iline += 1
            soper = LINES[iline].split("old")
            opr = soper[1]                          # opr
            iline += 1
            stest = LINES[iline].split("by")
            test = stest[1]                         # test
            iline += 1
            stestT = LINES[iline].split("monkey") 
            testT = int(stestT[1])                  # testT
            iline += 1
            stestF = LINES[iline].split("monkey")
            testF = int(stestF[1])                  # testF
            tmpM = Monkey(id)
            monkeys[id] = tmpM
            tmpM.items = items
            tmpM.opr = opr
            tmpM.test = test
            tmpM.testT = testT
            tmpM.testF = testF
    iline += 1
    if iline > len(LINES)-1: break

print("BEFORE monkey business starts:")
for m in monkeys:
    print(f"Monkey {m}: {monkeys[m].items}")

for r in range(1,rounds+1,1):
    print(f"- - - - - - - - - Round {r} - - - - - - - - -")

    for m in monkeys:
        tmpMitems = copy.deepcopy(monkeys[m].items)               # the items list changes real time, so we need a temp list
        # print(f"Monkey {m} {monkeys[m].insp}:")
        for i in tmpMitems:
            # print(f"\t--Inspect item {i}")
            monkeys[m].insp += 1
            opr = monkeys[m].opr.strip()
            sopr = opr.split()
            if len(sopr) == 1:
                wlevel = i * i
            elif sopr[0] == "*":
                wlevel = i * int(sopr[1])
            else: wlevel = i + int(sopr[1])
            if divisor > 1:
                wlevel = wlevel / divisor
            wlevel = math.floor(wlevel)
            test = int(monkeys[m].test)
            if (wlevel % test) == 0:
                toMonkey = monkeys[m].testT
            else:
                toMonkey = monkeys[m].testF
            monkeys[toMonkey].items.append(wlevel)  # add to receiving monkey
            monkeys[m].items.pop(0)
    for x in monkeys:
        print(f"Monkey {x}: inspected: {monkeys[x].insp}")


insplist = []
for m in monkeys:
    insplist.append(monkeys[m].insp)
# print(insplist)
max1 = max(insplist)
insplist.pop(insplist.index(max1))
max2 = max(insplist)
print(f"{PART}: Monkey buisiness level: {max1} * {max2} = {max1 * max2}")










        






