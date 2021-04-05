#the idea here is ordering the input and find 2 consecutive values with the same letter in the last position "LL" or "RR"

line1=""
line2=""

def seat_number(line):
    seat_number = 0
    print(line)
    for i in range(7):
        if line[i] == "B":
            seat_number += pow(2,(6-i))
            print(seat_number)
        print("line[" + str(i) + "]:" + line[i])
    seat_number = seat_number * 8
    for i in range(7,9):
        if line[i] == "R":
            seat_number += pow(2,(9-i))
            print(seat_number)
        print("line[" + str(i) + "]:" + line[i])
    return seat_number

first_line=True
for line in open("sorted-input.txt"):
    line2=line
    if not first_line and line2[9] == line1[9]:
        print("My seat is between " + line1.rstrip() + " and " + line2.rstrip())
        print(seat_number(line1.rstrip()))
        print(seat_number(line2.rstrip()))
    line1=line2
    first_line=False