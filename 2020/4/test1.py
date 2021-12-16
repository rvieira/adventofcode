input_file_name = "input.txt"
#output_file_name = "output.txt"
def line_is_not_empty(line):
    if line == "":
        return 0
    else:
        return 1

#output_file=open("output.txt","w")
aux_line = ""
for line in open(input_file_name):
    if line_is_not_empty(line.rstrip()) == 1:
        #print("not empty")
        #print("line: "+line)
        aux_line = aux_line.rstrip() + " " + line
        #print("aux_line: "+aux_line)
    else:
        #print("empty")
        print(aux_line.rstrip())
        aux_line = ""
print(aux_line)