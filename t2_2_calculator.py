# 1. 总价函数，新增 discount 默认参数
def get_total_price(price, qty, discount=1.0):
    return price * qty * discount

# 2. 分类函数（同上）
def classify_drug(price):
    if price > 100:
        return "高价药"
    else:
        return "常规药"

total_all = 0       # 累加合计
high_count = 0      # 高价药计数
normal_count = 0    # 常规药计数

for i in range(3):
    # 单价用 float()（支持小数，如 25.5）；数量用 int()
    price = float(input("请输入单价："))
    qty = int(input("请输入数量："))

    # 询问折扣：回车=不打折(1.0)，输入数字=打折
    d = input("折扣（直接回车表示不打折）：")
    if d == "":
        discount = 1.0
    else:
        discount = float(d)

    amount = get_total_price(price, qty, discount)   # 传入折扣
    category = classify_drug(price)                  # 分类
    total_all = total_all + amount                   # 累加合计
    if category == "高价药":                          # 计数
        high_count = high_count + 1
    else:
        normal_count = normal_count + 1

    print(f"第{i+1}笔：总价 {amount:.2f}，{category}（折扣 {discount}）")

print(f"三笔合计：{total_all:.2f}")
print(f"高价药 {high_count} 笔、常规药 {normal_count} 笔")