# 5 种药的库存数据（验收用）
drugs = [
    {"名称": "布洛芬",       "单价": 25.5,    "数量": 30},
    {"名称": "阿莫西林",     "单价": 12.0,    "数量": 50},
    {"名称": "奥希替尼",     "单价": 5580.0,  "数量": 2},
    {"名称": "维生素C",      "单价": 8.5,     "数量": 100},
    {"名称": "帕博利珠单抗", "单价": 17918.0, "数量": 1},
]

# 1. 循环 + 累加算总金额（单价 × 数量 求和）
total_value = 0
for drug in drugs:
    total_value = total_value + drug["单价"] * drug["数量"]

# 2. 擂台法：找单价最贵的药
most_expensive = drugs[0]        # 先假设第 1 个是擂主
for drug in drugs:
    if drug["单价"] > most_expensive["单价"]:
        most_expensive = drug     # 挑战者胜，更新擂主

# 3. 擂台法：找数量最多的药
most_qty = drugs[0]
for drug in drugs:
    if drug["数量"] > most_qty["数量"]:
        most_qty = drug

# 4. 打印结果
print(f"总金额：{total_value:.2f}")
print(f"最贵药品：{most_expensive['名称']}（单价 {most_expensive['单价']}）")
print(f"数量最多药品：{most_qty['名称']}（数量 {most_qty['数量']}）")