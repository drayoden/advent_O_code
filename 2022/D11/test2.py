import fileinput, os, sys
import re, pprint as pp

LINES = "".join(fileinput.input())
insp = ()
monkeys = {}  # dict

# get the monkey input...
for monkey in LINES.split(os.linesep * 2):  # divides monkeys between '\r\n'
    m = monkey.splitlines() # divides the lines of each monkey
    id = int(re.findall(r'[0-9]+',m[0])[0])
    items = re.findall(r'[0-9]+',m[1])
    opr = m[2].split("old")[1]
    div = int(re.findall(r'[0-9]+',m[3])[0])
    true = int(re.findall(r'[0-9]+',m[4])[0])
    false = int(re.findall(r'[0-9]+',m[5])[0])
    monkeys[id] = items,opr,div,true,false

pp.pprint(monkeys)

insp = ([0]*len(monkeys))
print(insp)

item = 1501
print(item)
item = item % 96577
print(item)


