#!/usr/bin/python3.8

import re

# abtgljhemltsdzlum



# nice string rules:
# contains: 3 vowels (aeiou) min, can repeate; 'aaa'
# contains: at least one double letter; 'xx' or 'bb', etc.
#   'aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz'
# does NOT contain: ab, cd, pq, or xy

print(f"Santa's nice list:\n" + "-"*30)
f = open('input.txt','r')
# kid = 'klajhemllcctasdzluimiiipx'
regnot = re.compile('^.{0,}(ab|cd|pq|xy)',re.I)
regdouble = re.compile('^.{0,}(aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz)',re.I)
vowelpat = re.compile(r'(a|e|i|o|u)',re.I)
nice = 0

# iterate through file:
for kid in f:
    kid = kid.strip()
    # does NOT contain: ab, cd, pq, or xy
    if not regnot.match(kid):   # outside logic, every thing else is in the scope of this 'if'

        # contains: at least one double letter; 'xx' or 'bb', etc.j
        if regdouble.match(kid):

            # contains: 3 vowels (aeiou) min, can repeate; 'aaa', or be spre4ad out; 'ksljfkadkelsjfislsl' -- contains 'aei'
            if len(re.findall(vowelpat,kid)) >= 3:

                print(f'{kid}: Nice!')
                nice += 1

print(f'Nice kids: {nice}')
f.close()




