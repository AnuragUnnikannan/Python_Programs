p = int(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))


# compound interest formula
a = p*pow((1+r/100), t)
interest = a-p
# display compound interest
print("Interest = %f"%(interest))
