input_file_path='/Users/ricardovieira/github/adventofcode/2022/day05/input_.txt'
stacks=['VCDRZGBW',' GWFCBSTV',' CBSNW',' QGMNJVCP',' TSLFDHB',' JVTWMN',' PFLCSTG',' BDZ',' MNZW']

def move_crates(n,n1,n2):
    crates_to_move=stacks[n1-1][n*(-1):]
    stacks[n1-1]=stacks[n1-1][:n*(-1)]
    stacks[n2-1]=stacks[n2-1]+crates_to_move

for line in open(input_file_path):
    n = int(line.split()[1])
    source_stack = int(line.split()[3])
    target_stack = int(line.split()[5])
    move_crates(n,source_stack,target_stack)
print(stacks)