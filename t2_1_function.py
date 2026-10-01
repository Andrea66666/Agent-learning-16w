def greet(name):
    print(f"你好，{name}")
greet("小明")
greet("小红")

def calc_total(price, qty):
    return price * qty

total = calc_total(25.5, 3)

print(f"总价是：{total}")

def classify_drug(price):
    if price > 100:
        return "高价药"
    else:
        return "常规药"

medicines = [
    {"名称": "布洛芬", "单价": 25.5},
    {"名称": "特效药", "单价": 200},
    {"名称": "维生素C", "单价": 8.5},
]

for med in medicines:
    result = classify_drug(med["单价"])
    print(f"{med['名称']}：{result}")