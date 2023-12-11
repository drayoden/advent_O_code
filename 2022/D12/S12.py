import fileinput

# Hill Climbing
# input: height map grid with a-z (low-high)
# S = my current position - elevation(a)
# E = my destination - elevation(z)
# I can only move one grid element (UDLR) that is one higher (a->b, h->i, ) 
#
