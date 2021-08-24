section = input()
roll = []
name = []
grade = []
count = []
gpa = []
g = 0
while(True):
    if section=="Courses":
        str = input()
        if '~' not in str:
            section = str
            continue
        tmp = str.split('~')
    elif section=="Students":
        str = input()
        if '~' not in str:
            section = str
            continue
        tmp = str.split('~')
        roll.append(tmp[0])
        name.append(tmp[1])
        grade.append(0)
        count.append(0)
        gpa.append(0)
    elif section=="Grades":
        str = input()
        if '~' not in str:
            section = str
            continue
        tmp = str.split('~')
        for i in range(len(roll)):
            if tmp[3]==roll[i]:
                if tmp[4]=="A":
                    g = 10
                elif tmp[4]=="AB":
                    g = 9
                elif tmp[4]=="B":
                    g = 8
                elif tmp[4]=="BC":
                    g = 7
                elif tmp[4]=="C":
                    g = 6
                elif tmp[4]=="CD":
                    g = 5
                elif tmp[4]=="D":
                    g = 4
                grade[i] = grade[i] + g
                count[i] = count[i] + 1
    elif section=="EndOfInput":
        break
for i in range(len(grade)):
    if count[i]!=0:
        gpa[i] = round(float(grade[i]/count[i]), 2)
    else:
        gpa[i] = 0
fd = {roll[i]: [name[i], gpa[i]] for i in range(len(roll))}
for k, v in sorted(fd.items()):
    print(k+'~', end='')
    for i in range(len(v)):
        if i!=len(v)-1:
            print(v[i], '~', sep='', end='')
        else:
            print(v[i], end='')
    print()
