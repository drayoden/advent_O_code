import sys
import itertools

stream = sys.stdin.read()

buff = []
foundit = 0
buffsize = 3 # base0 actually 4

for i, c in enumerate(stream):

    #fill the buffer with four chars from the stream
    buff.append(c)
    if i >= buffsize:
        print(buff)
        diff = True
        for x,y in itertools.combinations(buff,2):
            # print(x,y)
            if x == y:
                diff = False
                break
        if diff:
            foundit = i
            break
        buff.pop(0) # remove first element of list
        

if foundit != 0: 
    print("marker found at " + str(foundit + 1))
else:
    print("no marker found...")    
        
        
    

