medicines = ["布洛芬", "阿莫西林", "维生素C", "感冒灵", "蒙脱石散"]
for med in medicines:
    print(med)
for n in range(3):
     print(f"第 {n + 1} 次给患者发提醒")
medicines = [
    {"名称": "布洛芬", "单价": 25.5, "数量": 3},
    {"名称": "阿莫西林", "单价": 12.0, "数量": 5},
    {"名称": "维生素C", "单价": 8.5, "数量": 10},
]

total = 0  

for med in medicines:
    amount = med["单价"] * med["数量"]
    print(f"{med['名称']} 总价：{amount}")
    total = total + amount 

print(f"所有药总金额：{total}")