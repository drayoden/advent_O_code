import re

# nice: qjhvhtzxzqqjkmpb --> 'qj' appears twice, contains 'zxz'
# nice: xxyxx --> 'xx' appears twice, contains 'xyx' -- the two different rules over lap but niether rule overlaps itself.
# !nice: uurcxstgmygtbstg --> 'tg' appears twice, but the second rule is not met.
# !nice: ieodomkazucvgmuy --> contains 'odo', but no letter pair that appears twice.

# attempt 1: 77 wrong!

# rule two regex pattern: 'a.a|b.b|c.c|d.d|e.e|f.f|g.g|h.h|i.i|j.j|k.k|l.l|m.m|n.n|o.o|p.p|q.q|r.r|s.s|t.t|u.u|v.v|w.w|x.x|y.y|z.z'

# rule 2 regex pattern works:
r2regp = re.compile(r'^.{0,}(a.a|b.b|c.c|d.d|e.e|f.f|g.g|h.h|i.i|j.j|k.k|l.l|m.m|n.n|o.o|p.p|q.q|r.r|s.s|t.t|u.u|v.v|w.w|x.x|y.y|z.z)',re.I)
triplepat = re.compile(r'(aaa|bbb|ccc|ddd|eee|fff|ggg|hhh|iii|jjj|kkk|lll|mmm|nnn|ooo|ppp|qqq|rrr|sss|ttt|uuu|vvv|www|xxx|yyy|zzz)',re.I)

f = open('input.txt','r')
nice = 0
triples = 0

print(f"Santa's nice list:\n" + "-"*30)
#kid = 'qjhvhtzxzqqjkmpb'
#kid = 'xxyxx'


for kid in f:
    kid = kid.strip()   # remove new line
    triples = 0  # reset triples

    if r2regp.match(kid):

        # rule 1 regex pattern to find all 2 character words and if any match...
        r1 = re.findall(r'([a-z]{2}).*?',kid)
        kidt = '-' + kid
        r2 = re.findall(r'([a-z-]{2}).*?',kidt)
        r2.pop(0)
        r3 = set(r1 + r2)
        # print(f'R1:{len(r1)} R2:{len(r2)} R3:{len(r3)}')

        # if there are any triples, subtract them (overlap):
        triples = len(re.findall(triplepat,kid))

        if (len(r1) + len(r2) - triples ) > len(r3):
            nice += 1 
            print(f'{kid} -- nice! - [{nice}]')

print(f'Nice kids: {nice}')
f.close()



