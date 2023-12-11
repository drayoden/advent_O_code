import sys

DATA = open(sys.argv[1]).read().strip()
lines = DATA.split('\n')
totalpoints = 0
cards = []


for l in lines:
    card,nums = l.split(':')
    (_,cnum) = card.split()
    (wn,mn) = nums.split('|')
    wnums = wn.split()
    mynums = mn.split()
    matches = set(wnums).intersection(mynums)
    Lmatches = len(matches)

    points = 0
    

    # process card
    if Lmatches > 0:
        points = 1
        for i in range(Lmatches-1):
            points *= 2

        # add card copies    
        for j in range(Lmatches):
            cards.append(int(cnum)+1+j) 
            print(f'\t+{int(cnum)+1+j}')

    print(f'\tfound {cards.count(int(cnum))} copies of card {cnum}')

    for _ in range(cards.count(int(cnum))): 
        for k in range(Lmatches):
            cards.append(int(cnum)+1+k)
            print(f'\t+[{int(cnum)+1+k}]')
   
    # add original card:
    cards.append(int(cnum))

    print(f'[{cnum}]--{wnums} {mynums} - m{Lmatches} - p{points}\n')

    totalpoints += points

print(f'part1: {totalpoints}')
print(f'part2: {len(cards)}')

# par1: 23441  huzzah!
