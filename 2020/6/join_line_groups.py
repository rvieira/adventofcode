input_file_name = "input.txt"

def line_is_not_empty(line):
    if line == "":
        return 0
    else:
        return 1

aux_line = ""
for line in open(input_file_name):
    if line_is_not_empty(line.rstrip()) == 1:
        aux_line = aux_line.rstrip() + line
    else:
        print(aux_line.rstrip())
        aux_line = ""
print(aux_line)