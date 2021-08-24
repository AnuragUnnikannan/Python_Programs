# All these values are given
gems_list = ['Emerald', 'Ivory', 'Jasper', 'Ruby', 'Garnet']
price_list = [1760, 2119, 1599, 3920, 3999]
reqd_gems = ['Ivory', 'Emerald', 'Garnet']
reqd_quantity = [3, 10, 12]

menu = {}
# Assigning the price of gems to the corresponding gems
for i in range(len(gems_list)):
    c = gems_list[i]
    menu[c] = price_list[i]

price = 0.0  # to store total price
for i in range(len(reqd_gems)):
    c = reqd_gems[i]
    if c in menu.keys():  #checking whether that gem is in menu or not
        price = price + menu[c]*reqd_quantity[i]

# If price more than 30000 then 5% discount or 95% of the price
if price > 30000:
    price = float(0.95*price)
print(price)