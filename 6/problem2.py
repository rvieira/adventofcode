l1 = []
line_count = 0
total=0

def process(list_in):
    all_answered = 0
    #print(len(list_in))
    if len(list_in) > 1:
        print(list_in[0])
        print(len(list_in[0]))
        for i in range(0,len(list_in[0])-1):
            answer_count = 1
            print("i"+str(i))
            print(list_in[0][i])
            for j in range(1,len(list_in)-1):
                #print(list_in[0][i])
                #print(list_in[j])
                if list_in[0][i] in list_in[j]:
                    answer_count += 1
            #print("answer count: "+str(answer_count))
            #print("length: "+ str(len(list_in)))
            if answer_count == len(list_in):
                all_answered += 1
    else:
        all_answered = len(list_in[0])
    print(all_answered)
    return all_answered


for line in open('input.txt'):
    if len(line.rstrip()) > 0:
        #print("!!!AAA!!!")
        line_count += 1
        #print(line.rstrip())
        l1.append(line.rstrip()) # remove repeated
    else:
        #print("!!!BBB!!!")
        #print(process(l1))
        total += process(l1)
        l1=[]
        line_count = 0
print("TOTAL")
print(total)