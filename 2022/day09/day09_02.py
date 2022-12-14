Head_X=Head_Y=Tail_X=Tail_Y=1
rope=[[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
visited=[(1,1)]

def record_tail_pos():
    global visited
    if (rope[9][0],rope[9][1]) not in visited:
        visited.append((rope[9][0],rope[9][1]))

def tail_follow():
    global rope

    for i in range(len(rope)-1):
        if rope[i][0]-rope[i+1][0]>1:
            if rope[i][1]>rope[i+1][1]:
                rope[i+1][1]+=1
            if rope[i][1]<rope[i+1][1]:
                rope[i+1][1]-=1
            rope[i+1][0]+=1
        if rope[i][0]-rope[i+1][0]<-1:
            if rope[i][1]>rope[i+1][1]:
                rope[i+1][1]+=1
            if rope[i][1]<rope[i+1][1]:
                rope[i+1][1]-=1
            rope[i+1][0]-=1
        if rope[i][1]-rope[i+1][1]>1:
            if rope[i][0]>rope[i+1][0]:
                rope[i+1][0]+=1
            if rope[i][0]<rope[i+1][0]:
                rope[i+1][0]-=1
            rope[i+1][1]+=1
        if rope[i][1]-rope[i+1][1]<-1:
            if rope[i][0]>rope[i+1][0]:
                rope[i+1][0]+=1
            if rope[i][0]<rope[i+1][0]:
                rope[i+1][0]-=1
            rope[i+1][1]-=1
    
def move(direction,steps):
    for i in range(steps):
        if direction=='R':
            rope[0][0]+=1
        if direction=='L':
            rope[0][0]-=1
        if direction=='U':
            rope[0][1]+=1
        if direction=='D':
            rope[0][1]-=1
        tail_follow()
        record_tail_pos()

def rope_max_x():
    return(20)

def rope_max_y():
    return(20)

def print_grid():
    node_match=False
    for j in range(rope_max_y()*-1,rope_max_y()):
        for i in range(rope_max_x()*-1,rope_max_x()):
            for z in range(len(rope)):
                node_match=False
                if rope[z][0] == i+1 and rope[z][1] == j+1:
                    print(z,end='')
                    node_match=True
                    break
            if not node_match:
                print('.',end='')
        print()
    print()

for line in open('/Users/ricardovieira/github/adventofcode/2022/day09/input.txt','r'):
    move(line.strip().split()[0],int(line.strip().split()[1]))   
#    print_grid()
print(visited)
print(len(visited))