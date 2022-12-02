totalscore=score=i=0
for line in open('/Users/ricardovieira/github/adventofcode/2022/day02/input.txt'):
    score=0
    i+=1
    if line.split()[0] == "A": # Rock
        score+=1
        if line.split()[1] == "X": # Rock
            score+=3
        elif line.split()[1] == "Y": # Paper
            score+=0
        else: # Scissor
            score+=6
    elif line.split()[0] == "B": # Paper
        score+=2
        if line.split()[1] == "X": #Rock
            score+=6
        elif line.split()[1] == "Y": # Paper
            score+=3
        else: # Scissor
            score+=0
    else: # Scissor
        score+=3
        if line.split()[1] == "X": #Rock
            score+=0
        elif line.split()[1] == "Y": # Paper
            score+=6
        else: # Scissor
            score+=3
 #   print(score)
    totalscore+=score
    print(str(i)+': '+line+str(score)+','+str(totalscore))
#    print(totalscore)
print()
print(totalscore)
