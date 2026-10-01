import pandas as pd
df = pd.read_csv("inventory.csv", encoding="utf-8")
rows = df.to_dict("records")        # 变成 [{"名称":..., ...}, ...]
print("总行数：", len(rows))
# 统计1：总金额（单价 × 数量 累加）
total_value = 0
for row in rows:
    total_value = total_value + row["单价"] * row["数量"]
print("总金额：", total_value)

# 统计2：按类别计数（计数器 + 条件判断）
otc_count = 0
rx_count = 0
for row in rows:
    if row["类别"] == "OTC":
        otc_count = otc_count + 1
    else:
        rx_count = rx_count + 1
print("OTC 药品：", otc_count, "种")
print("处方药：", rx_count, "种")