initial_point=(500,0)

path_descriptions=['498,4 -> 498,6 -> 496,6','503,4 -> 502,4 -> 502,9 -> 494,9']
paths=[]
rock=[]

def load_segment(initx,inity,endx,endy):
    # it will load repeated rock coordinates but that is not a problem for this exercise
    if initx == endx:
        if inity<endy:
            for i in range(inity,endy+1):
                rock.append((initx,i))
        else:
            for i in range(inity,endy,-1):
                rock.append((initx,i))
    else:
        if initx < endx:
            for i in range(initx,endx+1):
                rock.append((i,inity))
        else:
            for i in range(initx,endx-1,-1):
                rock.append((i,inity))

def load_rocks(path):
    for i in range(len(path)-1):
        x0 = int(path[i].split(',')[0])
        y0 = int(path[i].split(',')[1])
        x1 = int(path[i+1].split(',')[0])
        y1 = int(path[i+1].split(',')[1])
        load_segment(x0,y0,x1,y1) 

def load_paths():
    for path_description in path_descriptions:
        paths.append(path_description.split(' -> '))
    for path in paths:
        # loop through all segments
        load_rocks(path)
    
def bottom():
    pass

def trickle_down():
    pass

load_paths()
print(paths)
print(rock)
for path in paths:
    for coord in path:
        print(coord.split(',')[0])
        print(coord.split(',')[1])
