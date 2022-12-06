input_file_path='/Users/ricardovieira/github/adventofcode/2022/day05/input_.txt'
stacks=['VCDRZGBW',' GWFCBSTV',' CBSNW',' QGMNJVCP',' TSLFDHB',' JVTWMN',' PFLCSTG',' BDZ',' MNZW']

def move_one_crate(n1,n2):
    crate=stacks[n1-1][-1:]
    stacks[n2-1]=stacks[n2-1]+crate
    stacks[n1-1]=stacks[n1-1][:-1]

def move_crates(n,n1,n2):
    for i in range(n):
        move_one_crate(n1,n2)

#print(stacks)
#move_crates(2,1,2)    
#print(stacks)
for line in open(input_file_path):
    n = int(line.split()[1])
    source_stack = int(line.split()[3])
    target_stack = int(line.split()[5])
    move_crates(n,source_stack,target_stack)
print(stacks)