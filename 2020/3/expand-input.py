def expand_line(input_str,number_of_times):
    result_str=input_str
    for _ in range(number_of_times):
        result_str=result_str+input_str
        #print(i+1)
        #print(result_str)
    return result_str

for line in open('input.txt'):
    print(expand_line(line.rstrip(),11))
#print(expand_line("abc",11))