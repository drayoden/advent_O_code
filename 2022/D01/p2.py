import sys
lines = sys.stdin.readlines()

# - list of 3 high values
# - remove mostCalsElf, nowElf -- don't need these
# - function: one input value, iterrates list and replaces lowes value if 
#   input value is greater

# list of three highest values
mostCals = [0,0,0]
nowCals = 0

def getMost(v):

    lmin = min(mostCals)

    if v > lmin:
        for i in range(3):
            if mostCals[i] == lmin:
                mostCals[i] = v
                break

for line in lines:
    x = line.rstrip()
    print(x)
   
    # at end of elf list
    if len(x) == 0: 

        # pass nowCals to getMost
        getMost(nowCals)    
        nowCals = 0    
    else:
        nowCals += int(x)

print(mostCals)
print(sum(mostCals))

    