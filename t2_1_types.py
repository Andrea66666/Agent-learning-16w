drug_name = "奥希替尼"
unit_price = 5580 
quantity = 3
discount = 0.75
covered = True
print(drug_name)
print(unit_price)
print(discount)
print(covered)
print(quantity)
print(type(drug_name))
print(type(unit_price))
print(type(discount))
print(type(covered))
print(type(quantity))
total_price = unit_price*quantity
print(f"总价是:{total_price}")
discounted_price = unit_price*discount*quantity
print(f"折扣价是:{discounted_price}")