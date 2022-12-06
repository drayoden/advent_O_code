import sys


mostCalsElf = 0
mostCals = 0

nowCals = 0 
nowElf = 0

for line in sys.stdin:
    x = line.rstrip()
    
    # at end of elf list
    if len(x) == 0: 

        # check if we have a new high 
        if (nowCals > mostCals ): 
            mostCals = nowCals
            mostCalsElf += 1
        nowElf += 1
        print("Elf: " + str(nowElf) + " [" + str(nowCals) + "]")
        nowCals = 0
    else:
        nowCals += int(x)

print("Winner Elf: " + str(mostCalsElf) + " [" + str(mostCals) + "]")

    