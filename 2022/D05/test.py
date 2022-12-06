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

ncut = 3
print(Stacks[0])
print(Stacks[1])

cutidx = len(Stacks[0]) - ncut


# move 3 from stack1 to stack2 (keep order)
cut = Stacks[0][cutidx::1]  # get last n start at 5 (0base)
print("cut: " + str(cut))
Stacks[0] = Stacks[0][0:cutidx:1] # replace original stack after removing crates
Stacks[1].extend(cut)

print(Stacks[0])
print(Stacks[1])
