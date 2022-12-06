import re, sys, pprint

circuit = {}  # set

for line in sys.stdin:
    line = line.strip()
    
    # parse each line into one of the following:
    # word -> ouput
    # word word -> ouput
    # word word word -> ouput
    pline = (
        re.match(r'(\w+) -> (\w+)',line)
        or re.match(r'(\w+) (\w+) -> (\w+)',line)
        or re.match(r'(\w+) (\w+) (\w+) -> (\w+)',line)
    ).groups()

    # adds a key/val pair to the 'circuit' set
    # key = pline[-1] -> the last element of pline (output)
    # val = tuple that is made of everything left of '->' in each line
    circuit[pline[-1]] = pline[:-1] 

print('circuit set:')
pprint.pprint(circuit)

aa = circuit['aa'] # returns the tuple for the key 'aa' in the circuit set
print(f'aa: {aa}')

print(len(circuit))