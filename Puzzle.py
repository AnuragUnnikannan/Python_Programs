heads = int(input("Enter number of heads: "))
feet = int(input("Enter number of feet: "))
rabbit = 0
chicken = 0
f = 0
for i in range(heads+1):
    j = heads - i
    if 2*i + 4*j == feet:
        chicken = i
        rabbit = j
        f = 1
        break

if f==1:
    print('Chickens: ',chicken)
    print('Rabbits: ',rabbit)
else:
    print('No solution')