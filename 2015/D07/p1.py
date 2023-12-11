import sys, re
lines = sys.stdin.readlines()

# wire dictonary: ID,signal
wires = {}

# create dictionary of wires with ID and sig/exp
for l in lines:
    line = l.rstrip()
    print(line)
    exp, wid = re.search(r'(.*) -> (.*)', line).groups()
    
    # int or string
    sig = None 

    if 'NOT' in exp:
        sig =     
    




    #add to dictionary
    wires[wid] = sig
    


    match spaces:
        
        # direct signal to wire 
        case 0:
            signal = int(left)

        # NOT
        case 1:
            if left.split(' ')[0] == 'NOT':
                w = left.split(' ')[1]
                signal = ~wires.get(w) & 65535 # need to keep this a 16bit unsigned int...
        
        # AND/OR or LSHIFT/RSHIFT
        case 2: 
            if left.find("SHIFT") > 0:
                w = left.split(' ')[0]
                shift = left.split(' ')[1]
                num = left.split(' ')[2]
                
                if shift == 'LSHIFT':
                    signal = wires.get(w) << int(num)
                else:
                    signal = wires.get(w) >> int(num)

            else:
                w1 = left.split(' ')[0]
                gate = left.split(' ')[1]
                w2 = left.split(' ')[2]
                
                if gate == 'AND':
                    signal = wires.get(w1) & wires.get(w2)
                else:
                    signal = wires.get(w1) | wires.get(w2)

        # eight operators to identify:
        #   signal (integer)
        #   gates (AND,OR,NOT,LSHIFT,RSHIFT)
        #   wire (lc char(s))
        #   '->' left is "provided to" right
        #   right of arrow ('->') is ALWAYS a wire
        #   left of arrow is one of and will always result in an integer:
        #       wire gate wire (2spc)
        #       wire SHIFT # (2spc look for SHIFT)
        #       NOT wire (one space -> NOT)
        #       signal (no space on left)
        # python bitwise opers:
        #   AND: '&' -> x & y
        #   OR:  '|' -> x | y
        #   NOT: '~' -> ~x
        #   LSHIFT: '<<' -> x << 1 OR x << 2...
        #   RSHIFT: '>>' -> x >> 1 OR x >> 2...
    
    # add/update wire:
    wires[wire] = signal
    print(wires)
    print()

print("wire a :" + str(wires.get('a')))
    

