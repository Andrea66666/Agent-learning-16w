# Agent 开发 16 周计划 - 学习仓库

> Agent 开发 16 周计划（Python + 医药数据场景）的学习仓库，从零开始记录 Python 从基础语法到文件读取的每一步练习与里程碑。

## 目录结构

| 文件 | 用途 |
|------|------|
| `hello.py` | T1.3 第一个 Python 程序（打印入门） |
| `t2_1_types.py` | T2.1 变量与类型练习：定义变量、`type()` 查看类型、f-string 打印总价/折后价 |
| `t2_1_condition.py` | T2.1 条件判断练习：`input()` 输入单价、判断"高价药/常规药"、医保覆盖三分类 |
| `t2_1_function.py` | T2.1 函数练习：定义 `greet`、`calc_total`（含 `return`） |
| `t2_1_loop.py` | T2.1 循环练习：`for` 循环打印药名、`for + range` 打印提醒 |
| `t2_1.py` | T2.1 综合：药品订单结算（函数 + 循环输入 3 笔 + 累加合计） |
| `t2_2_calculator.py` | T2.2 药品订单结算小工具：默认参数、折扣输入、累加、统计高价/常规药笔数 |
| `t2_3_inventory.py` | T2.3 库存统计：5 种药字典列表、累加总金额、擂台法找最贵/最多药品 |
| `t3_1_dict.py` | T3.1 字典练习：键值访问、`items()` 遍历、列表 `append`、元组 |
| `inventory.csv` | 数据文件：8 种药品的库存表（名称/类别/单价/数量） |
| `t3_2_csv.py` | T3.2 读 CSV：`pandas` 读入 → 转字典列表 → 统计总金额、按类别计数 |
| `t3_3_pdf.py` | T3.3 读 PDF：`pymupdf` 打开 PDF、提取并打印首段文字 |
| `t3_file_io.py` | T3.4 里程碑整合：CSV 统计报告 + PDF 首段文字，一个脚本完成 |
| `2025年度药品审评报告.pdf` | 数据文件：`t3_3_pdf.py` / `t3_file_io.py` 读取的 PDF（数据来源） |

## 如何运行

本项目依赖装在虚拟环境 `venv` 里（Python 3.14.7 + pandas + PyMuPDF），**必须用 venv 的 Python 运行**。

### 1. 激活虚拟环境

在项目目录打开终端（PowerShell）：

```powershell
F:\Agent-learning-16w\venv\Scripts\Activate.ps1
```

激活成功后终端行首会出现 `(venv)` 标记。也可以按 `Ctrl+Shift+P` → `Python: Select Interpreter` 选择 venv 解释器。

> 提示：若 `pip` 命令报 `Fatal error in launcher`，改用 `python -m pip ...`（venv 曾从 D 盘迁移到 F 盘所致）。

### 2. 运行脚本

```powershell
# 基础练习
python hello.py

# T2 结算 / 库存
python t2_2_calculator.py   # 需要交互输入单价、数量
python t2_3_inventory.py

# T3 文件读取
python t3_2_csv.py          # 读取 inventory.csv（需同目录）
python t3_3_pdf.py          # 读取 2025年度药品审评报告.pdf（需同目录）
python t3_file_io.py        # 里程碑整合：CSV 统计 + PDF 提取
```

**注意：** `t3_2_csv.py` / `t3_3_pdf.py` / `t3_file_io.py` 运行前，确认数据文件（`inventory.csv`、`2025年度药品审评报告.pdf`）与脚本在同一目录。

## 已学技能清单

**语法与逻辑**
- 变量与 `type()` 类型查看
- 条件判断 `if / else`（冒号 + 缩进构成代码块）
- 循环 `for`、`for + range`（从 0 起、用 `range(1,4)` 或 `n+1` 显示从 1 开始）
- 函数定义 `def`、`return`、默认参数（`discount=1.0`）
- 累加器、计数器、擂台法（找最大值/最多）
- f-string 字符串格式化（`f"总价是：{x}"`）
- `input()` 用户输入、`int()` / `float()` 类型转换

**数据结构**
- 列表（遍历、`append` 变长）
- 字典（键值访问、`in` 判断、`items()` 遍历）
- 元组（只读，不可修改）
- 字典列表（`[{"名称":..., ...}, ...]` 复合结构）

**文件读取**
- CSV：`pandas.read_csv(..., encoding="utf-8")` → `to_dict("records")` 转字典列表
- PDF：`pymupdf.open(...)` → `page.get_text()` 提取文字

**开发环境与工具**
- 虚拟环境 venv 的创建、激活、迁移
- `pip` / `python -m pip` 安装依赖（pandas、PyMuPDF）
- Git 与 GitHub：`git add` / `commit` / `push`，分支同步，远程仓库管理

---

**进度**：T1 入门 → T2 类型/条件/循环/函数 → T3 数据结构与文件读取（已全部推送至 GitHub）。
