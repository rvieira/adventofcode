lines=[]
valid_pwd=0
#def count_chars(target_char,pwd)
#    result=0
#    for char in pwd:
#        if char==target_char:
#            result+=1

for line in open('input.txt'):
    pwd_policy,target_char,pwd=line.split()
    pwd_policy_min,pwd_policy_max=pwd_policy.split('-')
    target_char=target_char[0]
    lines.append(line)
    print('min: '+pwd_policy_min+'; max: '+pwd_policy_max+'; policy: '+pwd_policy+'; char: '+target_char+'; pwd: '+pwd)
    occurrences=pwd.count(target_char)
    print(occurrences)
    if occurrences >= int(pwd_policy_min) and occurrences <= int(pwd_policy_max):
        valid_pwd+=1
        print("good")
    else:
        print("bad")    
    #print(line)
print (len(lines))
print(valid_pwd)