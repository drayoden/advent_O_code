import sys
lines = sys.stdin.readlines()

# attempt 1: 1145908 -- nope! too low

maxsize = 100000
fscapacity = 70000000
updatefreespace = 30000000

class Inode:
    def __init__(self, name: str, size=0):  # size=0 id default for dirs
        self.name = name
        self.size = size
        self.child = [] # list of child objects: file or directory
        self.parent = Inode
    
    def __str__(self):   # a readable version of objet
        children = ''
        if self.child:
            for c in self.child:
                children += f"({c.name}|{c.size})"
        return f"name:({self.name}) size:({self.size}) c:[{children}]"

cwd = [] # list for current working directory
firstinode = Inode

for i, l in enumerate(lines):
    line = l.rstrip()
    # is this line a command?
    if line.startswith('$'):
        print(f"cmd: {line}")
        sline = line.split()

        if sline[1] == 'cd':
            if sline[2] == "..":
                cwd.pop(len(cwd)-1)
                currentinode = currentinode.parent

            # change to a dir - needs to be a child of the current inode
            else: 
                dname = sline[2]
                cwd.append(dname)   # do I need cwd?
                tmpinode = Inode(dname)  # new inode use default size=0
                
                if i == 0:
                    currentinode = tmpinode
                    firstinode = currentinode # keep the first inode, this is the entry to the hierarchy
                    firstinode.parent = None
                else:
                    tmpinode.parent = currentinode
                    currentinode.child.append(tmpinode)
                    currentinode = tmpinode
                    
            # print(f"cwd:{cwd}")

    # not a command; listing (ls) the directory - only create new inodes for files 
    else:
        sline = line.split()
        info = ''
        if sline[0] != 'dir': 
            size,fname = sline    # this is a file with a size
            info = f"new file inode: {fname}:{size}"
            currentinode.child.append(Inode(fname,int(size))) # add file to currentnode child list
        print(f"ls: {line} -- {info}")

print("input complete...")
print("set the directory sizes...")

def setDsize(inode):
    dirsize = 0
    if inode.child:
        for c in inode.child:
            if c.size != 0: # this is a file
                dirsize += c.size
            else:
                dirsize += setDsize(c) # this is a directory we need to get it's child list
    
    inode.size = dirsize
    # print(inode)
    return dirsize

setDsize(firstinode)

total = 0

print(f"\n\n\nFinding directories with size <= {maxsize}...")

total = 0
deldirsize = 0
largest = 0


def findMax(inode):
    global total
    global deldirsize
    global largest
    if inode.child:
        print(f"{inode.name}-{inode.size}")
        if inode.size <= maxsize: total += inode.size
        if inode.size > largest: largest = inode.size
        for c in inode.child:
            if c.child:
                findMax(c)

findMax(firstinode)

deldirsize = [] # get a list of directories that would work then get a min()

spaceneeded = fscapacity - updatefreespace
freespace = fscapacity - largest


def findDirMin(inode):
    global deldirsize
    if inode.child:
        thisinodesize = inode.size
        if (thisinodesize + freespace) >= updatefreespace:
            deldirsize.append(thisinodesize)
            for c in inode.child:
                findDirMin(c)

findDirMin(firstinode)
print(deldirsize)

print(f"P1 -- Total: {total}")
print(f"P2 -- largest directory: {largest}")
print(f"current freespace: {freespace}")
print(f"space needed to perform update: {updatefreespace}")
print(f"P2 -- Size of directory to delete: {min(deldirsize)}")



















