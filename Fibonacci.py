x = -1
y = 1
n = int(input())
for i in range(0, n):
    z = x+y
    if(i<n-1):
        print(z, end=', ')
    else:
        print(z, end='')
    x = y
    y = z
