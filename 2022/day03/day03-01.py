total=0
characters='.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def lefthalf(line):
    line_length = len(line)
    return(line[:int(line_length/2)])

def righthalf(line):
    line_length = len(line)
    return(line[int(line_length/2):])

def priority(line):
    line = line.strip()
    left = lefthalf(line)
    right = righthalf(line)
    for character in left:
        if character in right:
            return(characters.find(character))


for line in open('/Users/ricardovieira/github/adventofcode/2022/day03/input.txt'):
    total+=priority(line)
print(total)