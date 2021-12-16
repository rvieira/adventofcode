input_file_name = "joined-lines-input.txt"

def removeDuplicate(str_in): 
    aux_str=""
    n = len(str_in)
    print("original:"+str_in)
    print("initial size:"+str(n))
    for i in range(0, n): 
        for j in range(0, i + 1): 
            if (str_in[i] == str_in[j]): 
                break
        if (j == i): 
            aux_str = aux_str + str_in[i] 
    print("aux_str:"+aux_str)
    return aux_str 

yes_answers=0
for line in open (input_file_name):
    auxline = removeDuplicate(line)
    print(auxline.rstrip() + str(len(auxline.rstrip())))
    yes_answers += len(auxline.rstrip())
print(yes_answers)