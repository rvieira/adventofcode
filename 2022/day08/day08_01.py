trees=[]
visible_trees=0

def load_trees():
    for line in open('/Users/ricardovieira/github/adventofcode/2022/day08/input.txt'):
        trees.append(line.strip())

def tree_is_visible(x,y):
    visible_up=visible_down=visible_left=visible_right=True
    # check_up
    for i in range(0,y):
        if int(trees[i][x]) >= int(trees[y][x]):
            visible_up=False 
    # check_down
    for i in range(y+1,len(trees)):    
        if int(trees[i][x]) >= int(trees[y][x]):
            visible_down=False
    # check_left
    for i in range(0,x):    
        if int(trees[y][i]) >= int(trees[y][x]):
            visible_left=False
    # check_right
    for i in range(x+1,len(trees[y])):    
        if int(trees[y][i]) >= int(trees[y][x]):
            visible_right=False
    return(visible_right or visible_left or visible_up or visible_down)


load_trees()
visible_trees = len(trees)*2 + (len(trees[0])*2-4)
for i in range(1,len(trees[0])-1):
    for j in range(1,len(trees)-1):
        if tree_is_visible(i,j):
            visible_trees+=1
print(visible_trees)