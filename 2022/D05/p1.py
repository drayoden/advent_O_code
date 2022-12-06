import sys
lines = sys.stdin.readlines()

# move one crate at a time

Stacks = [
    ['Q','F','M','R','L','W','C','V'],
    ['D','Q','L'],
    ['P','S','R','G','W','C','N','B'],
    ['L','C','D','H','B','Q','G'],
    ['V','G','L','F','Z','S'],
    ['D','G','N','P'],
    ['D','Z','P','V','F','C','W'],
    ['C','P','D','M','S'],
    ['Z','N','W','T','V','M','P','C']
]

for l in lines:
    line = l.rstrip()
    sline = line.split(' ')

    moves = int(sline[1])
    sfrom = int(sline[3]) - 1   # base 0 lists
    sdest = int(sline[5]) - 1   # base 0 lists

    # print("F: " + str(Stacks[sfrom]))
    # print("T: " + str(Stacks[sdest]))

    for i in range(moves):
        cpop =  Stacks[sfrom].pop(len(Stacks[sfrom])-1)
        Stacks[sdest].append(cpop)
        
    print("MOV:" + str(moves) + " F:" + str(sfrom) + " T:" + str(sdest))
    # print("F: " + str(Stacks[sfrom]))
    # print("T: " + str(Stacks[sdest]))
    # print() 

i = 1
crates = []   
for s in Stacks:
    lastcrate = s[len(s) - 1]
    print("Stack" + str(i) + ": " + str(s) + " Top crate: " + lastcrate)
    i += 1
    crates.append(lastcrate)

print("Top crates: " + ''.join(crates))