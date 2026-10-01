drug = {"名称": "奥希替尼", "单价": 5580.0, "数量": 2}

# ① 取键值 + in 判断键是否存在
print(drug["名称"], "单价" in drug)

# ② items() 遍历键值对
for key, value in drug.items():
    print(key, value)

# ③ 列表的 append 追加（列表可以变长）
names = []
names.append("布洛芬")
names.append("奥希替尼")
print(names, len(names))

# ④ 元组：只读的"列表"，不能修改（一行了解即可）
point = (3, 4)
print(point[0])