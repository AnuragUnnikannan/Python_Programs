li = [4, 5, 6]
c = int(input())
k = int(input())
if c==1:
    print("Element",k,"inserted at right")
    li.append(k)
elif c==2:
    print("Element",k,"inserted at left")
    li.insert(0, k)
elif c==3:
    print("Element",li[0],"deleted from left")
    li.pop(0)
elif c==4:
    print("Element",li[2],"deleted from right")
    li.pop(2)
elif c==5:
    for i in range(len(li)):
        if i!=len(li)-1:
            print(li[i], "->", end='')
        else:
            print(li[i])
for i in range(len(li)):
        if i!=len(li)-1:
            print(li[i], "-> ", end='')
        else:
            print(li[i])