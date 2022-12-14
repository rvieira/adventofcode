Head_X=Head_Y=Tail_X=Tail_Y=1
visited=[(1,1)]

def record_tail_pos():
    global visited
    if (Tail_X,Tail_Y) not in visited:
        visited.append((Tail_X,Tail_Y))

def tail_follow():
    global Tail_Y,Tail_X
    if Head_X-Tail_X>1:
        if Head_Y!=Tail_Y:
            Tail_Y=Head_Y
        Tail_X+=1
    if Head_X-Tail_X<-1:
        if Head_Y!=Tail_Y:
            Tail_Y=Head_Y
        Tail_X-=1
    if Head_Y-Tail_Y>1:
        if Head_X!=Tail_X:
            Tail_X=Head_X
        Tail_Y+=1
    if Head_Y-Tail_Y<-1:
        if Head_X!=Tail_X:
            Tail_X=Head_X
        Tail_Y-=1
    
def move(direction,steps):
    global Head_X,Head_Y
    for i in range(steps):
        if direction=='R':
            Head_X+=1
        if direction=='L':
            Head_X-=1
        if direction=='U':
            Head_Y+=1
        if direction=='D':
            Head_Y-=1
        record_tail_pos()
        tail_follow()

def print_grid():
    pass

for line in open('/Users/ricardovieira/github/adventofcode/2022/day09/input.txt','r'):
    move(line.strip().split()[0],int(line.strip().split()[1]))   
print(visited)
print(len(visited))