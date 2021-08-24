def find_GCD(x, y):
    while(y):
        x, y = y, x%y
    return x
l = [2, 4, 6, 8, 16]
num1 = l[0]
num2 = l[1]
gcd = find_GCD(num1, num2)
for i in range(2, len(l)):
    gcd = find_GCD(gcd, l[i])
print(gcd)
