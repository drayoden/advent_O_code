
str = "abcdef012343"
lstr = len(str)
print(f'len(str): {lstr}')

for c in str:
    print(c)

print(f'str[0]: {str[0]}')
print(f'str[4]: {str[4]}')


print(f'None test...')
a = None
b = 0
# print(a < b)

lst = []

print(lst,len(lst))
def padlist(rlst,llen):
    return rlst + [0]*(llen - len(rlst))

nlst = padlist(lst,10)
print(nlst,len(nlst))








