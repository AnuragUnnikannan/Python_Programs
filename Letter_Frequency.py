s = input("Enter string: ")
d = {}
# removing all spaces
s = s.replace(' ', '')
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
print(d)