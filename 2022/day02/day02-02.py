totalscore=score=i=0
for line in open('/Users/ricardovieira/github/adventofcode/2022/day02/input.txt'):
    score=0
    i+=1
    if line.split()[1] == "X": # Lose
        score+=0
        if line.split()[0] == "A": # Rock, to lose I must choose Scissor 
            score+=3
        elif line.split()[0] == "B": # Paper, to lose I must choose Rock
            score+=1
        else: # Scissor
            score+=2
    elif line.split()[1] == "Y": # Draw
        score+=3
        if line.split()[0] == "A": #Rock
            score+=1
        elif line.split()[0] == "B": # Paper
            score+=2
        else: # Scissor
            score+=3
    else: # Win
        score+=6
        if line.split()[0] == "A": #Rock
            score+=2
        elif line.split()[0] == "B": # Paper
            score+=3
        else: # Scissor
            score+=1
 #   print(score)
    totalscore+=score
    print(str(i)+': '+line+str(score)+','+str(totalscore))
#    print(totalscore)
print()
print(totalscore)
