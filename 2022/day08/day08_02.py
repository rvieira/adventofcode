trees=[]
visible_trees=0

def load_trees():
    for line in open('/Users/ricardovieira/github/adventofcode/2022/day08/input.txt'):
        trees.append(line.strip())

def scenic_score(x,y):
    # check_up
    distance_up=1
    for i in range(y-1,0,-1):
        if int(trees[i][x]) >= int(trees[y][x]):
            break
        else:
            distance_up+=1 
    # check_down
    distance_down=1
    for i in range(y+1,len(trees)-1):    
        if int(trees[i][x]) >= int(trees[y][x]):
            break
        else:
            distance_down+=1
    # check_left
    distance_left=1
    for i in range(x-1,0,-1):    
        if int(trees[y][i]) >= int(trees[y][x]):
            break
        else:
            distance_left+=1
    # check_right
    distance_right=1
    for i in range(x+1,len(trees[y])-1):    
        if int(trees[y][i]) >= int(trees[y][x]):
            break
        else:
            distance_right+=1
    return(distance_right*distance_left*distance_up*distance_down)
#564300
load_trees()
highest_scenic_score=0
for i in range(1,len(trees[0])-1):
    for j in range(1,len(trees)-1):
        current_ss = scenic_score(i,j)
        if current_ss > highest_scenic_score:
            highest_scenic_score = current_ss        
print(highest_scenic_score)