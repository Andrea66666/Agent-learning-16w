# 1. 计算总价的函数
def get_total_price(price, qty):
    return price * qty

# 2. 分类函数
def classify_drug(price):
    if price > 100:
        return "高价药"
    else:
        return "常规药"

# 累加器：先初始化为 0
total_all = 0

# 3. 循环输入 3 笔
for i in range(3):
    price = int(input("请输入单价："))
    qty = int(input("请输入数量："))

    amount = get_total_price(price, qty)   # 调用函数算总价
    category = classify_drug(price)        # 调用函数分类
    total_all = total_all + amount         # 累加

    print(f"第{i+1}笔：总价 {amount}，{category}")

# 5. 最后打印合计
print(f"三笔合计：{total_all}")