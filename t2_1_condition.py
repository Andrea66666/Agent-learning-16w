price = int(input("请输入药品单价："))
if price > 100:
    print("高价药")
else:
    print("常规药")
covered = True
price = int(input("请输入药品单价："))
if not covered:
    print("自费药")
elif price > 100:
    print("医保覆盖的高价药")
else:
    print("医保覆盖的常规药")
price = int(input("请输入药品单价："))
quantity = int(input("请输入数量："))
if quantity > 10 and price > 100:
    print("批发量级高价药")
else:
    print("未达批发量级")