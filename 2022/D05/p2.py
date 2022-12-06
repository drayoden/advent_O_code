import sys
lines = sys.stdin.readlines()

# move all crates at once and retain order

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

    nmove = int(sline[1])
    sfrom = int(sline[3]) - 1   # base 0 lists
    sdest = int(sline[5]) - 1   # base 0 lists
    sidx = len(Stacks[sfrom]) - nmove  # slice index

    print("MOV:" + str(nmove) + " F:" + str(sfrom) + " T:" + str(sdest))

    cut = Stacks[sfrom][sidx::1] # get number of crates form top of sfrom stack
    Stacks[sfrom] = Stacks[sfrom][0:sidx:1] # replace sfrom stack after removing crates
    Stacks[sdest].extend(cut) # append sdest stack
        

i = 1
crates = []   
for s in Stacks:
    lastcrate = s[len(s) - 1]
    print("Stack" + str(i) + ": " + str(s) + " Top crate: " + lastcrate)
    i += 1
    crates.append(lastcrate)

print("Top crates: " + ''.join(crates))