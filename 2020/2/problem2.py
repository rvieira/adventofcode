valid_pwd=0
#def count_chars(target_char,pwd)
#    result=0
#    for char in pwd:
#        if char==target_char:
#            result+=1

for line in open('input.txt'):
    pwd_policy,target_char,pwd=line.split()
    pwd_pos1,pwd_pos2=pwd_policy.split('-')
    pos1=int(pwd_pos1)-1
    pos2=int(pwd_pos2)-1
    target_char=target_char[0]
    print('pos 1: '+str(pos1)+'; char 2: '+str(pos2)+'; policy: '+pwd_policy+'; char: '+target_char+'; pwd: '+pwd)
    if (pwd[pos1] == target_char) != (pwd[pos2] == target_char):
        valid_pwd+=1
        print("good")
    else:
        print("bad")    
    #print(line)
print(valid_pwd)