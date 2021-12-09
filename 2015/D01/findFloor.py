#!/usr/bin/python3.8

# "((())()("

go = ['(',')']

import sys

f = 0; i = 0; pos = 0

for inp in sys.stdin:
    for c in inp:
        i += 1
        if c in go:
            if c == '(': 
                f = f + 1
            else: 
                f = f - 1
            if f == -1 and pos == 0 :
                pos = i
            print ('F = ' + str(f))
print('pos: ' + str(pos))
        
