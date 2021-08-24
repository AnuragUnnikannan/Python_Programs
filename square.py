squareLambda = lambda x:x**2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_nums = []
for i in nums:
    square_nums.append(squareLambda(i))
print(square_nums)
