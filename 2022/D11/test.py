
monkeys = {} # monkey id dictionary

class Monkey:
    def __init__(self,id: int):
        self.id = id
        self.items = []
        self.opr = str
        self.test = int
        self.testT = int
        self.testF = int
    
    def __str__(self):
        return f"id:{self.id} items:{self.items} opr:{self.opr} test:{self.test} testT:{self.testT} testF:{self.testF}"
tmpM = Monkey

id = 0
m = Monkey(id)

# add this monkey to monkey dict:
monkeys[id] = m

m.items = (83,27)
m.opr = '* 4'
m.test = 7
m.testT = 2
m.testF = 4

print(monkeys)

id = 2
m = Monkey(id)

# add this monkey to monkey dict:
monkeys[id] = m

m.items = (12,56)
m.opr = '+ 2'
m.test = 3
m.testT = 1
m.testF = 0

print(monkeys)

print(monkeys[0])
print(monkeys[2])

# update items for monkey 0:
monkeys[0].items = (84,27,44)
print(monkeys[0])

str = "    Operation: new = old * 19"
sstr = str.split("old")
print(sstr)

print(eval('79 * 79'))


        
















