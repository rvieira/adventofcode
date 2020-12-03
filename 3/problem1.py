posx = -3
tree_count = 0
input_file_name='input.txt'

# for each line in the file move position 3 left, 1 down and check if there is a tree (#)
# in fact all I have to do is moving the horizontal pointer (posx) as the line is consumed at every iteraction
# because the pattern repeats itself all I have to do is add mod 32 (line size)

for line in open(input_file_name):
    posx+=3
    posx = posx % 31
    print(line.rstrip())
    print(posx+1)
    print(line[posx])
    if line[posx] == "#":
        tree_count += 1
print("Trees: "+str(tree_count))