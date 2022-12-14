cycle_num=0
X=1

def process_line(line):
    global cycle_num
    global X

    cycle_num+=1
    signal_strength = cycle_num*X
    

for line in open('/Users/ricardovieira/github/adventofcode/2022/day10/input.txt'):
    process_line(line)