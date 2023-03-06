import math

copies = 60
bs_discount = 0.4
cost = 24.95
shipping = 3

total_cost = (copies * 0.4 * cost)
shipping_cost = shipping + (3 * 0.75 * 59)
total_expenditure = total_cost + shipping_cost

print(total_cost)
print(shipping_cost)
print(total_expenditure)