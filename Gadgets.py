gadgets = ['Mobile', 'Laptop', 100, 'Camera', 310.28, 'Speakers', 27.00, 'Television', 1000, 'Laptop Case', 'Camera Lens']
str_li = []
num_li = []
for i in gadgets:
    if isinstance(i, str):  #checking whether the element is a string or not
        str_li.append(i)
    else:
        num_li.append(i)
print("String List: ",str_li)
print("\nNumber List: ",num_li)
print("\nAscending String List: ",sorted(str_li))
print("\nDescending String List: ",sorted(str_li, reverse=True))
print("\nAscending Number List: ",sorted(num_li))
print("\nDescending Number List: ",sorted(num_li, reverse=True))