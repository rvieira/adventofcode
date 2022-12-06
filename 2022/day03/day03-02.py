total=linecount=groupcount=0
characters='.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def common_char(l1,l2,l3):
    for c1 in l1:
        if c1 in l2 and c1 in l3:
            return(c1)

with open('/Users/ricardovieira/github/adventofcode/2022/day03/input.txt') as file:
    lines = [line.rstrip() for line in file]
for i in range(0,len(lines),3):
    print(common_char(lines[i],lines[i+1],lines[i+2]))
    total+=characters.find(common_char(lines[i],lines[i+1],lines[i+2]))
print(total)