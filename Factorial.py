def fact(a):
    f = 1
    for i in range(1, a+1):
        f = f*i
    return f

n = int(input("Enter a number: "))
print("Factorial of {0} is {1}".format(n, fact(n)))
