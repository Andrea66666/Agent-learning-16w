import pandas as pd
import pymupdf

# ============ 第一部分：读 CSV，打印统计报告 ============
df = pd.read_csv("inventory.csv", encoding="utf-8")
rows = df.to_dict("records")

# 总金额（单价 × 数量 累加）
total_value = 0
for row in rows:
    total_value = total_value + row["单价"] * row["数量"]

# 按类别计数
otc_count = 0
rx_count = 0
for row in rows:
    if row["类别"] == "OTC":
        otc_count = otc_count + 1
    else:
        rx_count = rx_count + 1

print("===== CSV 统计报告 =====")
print("总行数：", len(rows))
print("总金额：", total_value)
print("OTC 药品：", otc_count, "种")
print("处方药：", rx_count, "种")

# ============ 第二部分：读 PDF，打印首段文字 ============
print("\n===== PDF 首段文字 =====")
doc = pymupdf.open("2025年度药品审评报告.pdf")
page = doc[0]
text = page.get_text()
print(text[:500])