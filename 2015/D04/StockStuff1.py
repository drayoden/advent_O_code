#!/usr/bin/python3.8

# input: bgvyzdsv
# abcdef + 609043 = abcdef609043,  hexdigest = 000001dbbfa...
# pqrstuv + 1048970 = pqrstuv1048970, hexdigest = 000006136ef....

# NOTE: part1 and part2 use the same code since it prints all hashes that start
# with at LEAST 5 zeros, there is ONE hash that starts with 6 zeros also

import hashlib, re

key = "bgvyzdsv"
max = 10000000
regp = re.compile('^0{5,}')   # at LEAST five starting zeros
# key = "abcdef609043"
# key = "pqrstuv1048970"

# for loop, 1 to max

for x in range(max + 1):
    xstr = str(x)
    keydnum = key + xstr
    # print(keydnum)
    r = hashlib.md5(keydnum.encode())
    # print(r); 
    rhex = r.hexdigest()  # string
    if regp.match(rhex):
        print(rhex + ' -- ' + xstr)




