i=j=0

def iscontained(line):
    a0=int(line.split(',')[0].split('-')[0])
    a1=int(line.split(',')[0].split('-')[1])
    b0=int(line.split(',')[1].split('-')[0])
    b1=int(line.split(',')[1].split('-')[1])
    if (a0 <= b0 and a1>=b1) or (b0 <= a0 and b1 >= a1):
        return(True)
    else:
        return(False)

def overlaps(line):
    a0=int(line.split(',')[0].split('-')[0])
    a1=int(line.split(',')[0].split('-')[1])
    b0=int(line.split(',')[1].split('-')[0])
    b1=int(line.split(',')[1].split('-')[1])
    if (a0 >= b0 and a0 <= b1) or (a1 >= b0 and a1 <= b1) or (b0 >= a0 and b0 <= a1) or (b1 >= a0 and b1 <= a1):
        return(True)
    else:
        return(False)

#for line in open('/Users/ricardovieira/github/adventofcode/2022/day04/example_input.txt'):
for line in open('/Users/ricardovieira/github/adventofcode/2022/day04/input.txt'):
    if iscontained(line.strip()): 
        i+=1
    if overlaps(line.strip()):
        j+=1
print(i, j)