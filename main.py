import tkinter as tk
from tkinter import messagebox

def calculate_profit(cost_price, sale_price, rate_percent):
    rate_decimal = rate_percent / 100.0
    rate_cost = sale_price * rate_decimal
    profit = sale_price - (cost_price + rate_cost)
    return profit

def calculate_sale_price(cost_price, desired_profit, rate_percent):
    rate_decimal = rate_percent / 100.0
    rate_cost = cost_price * rate_decimal
    sale_price = cost_price + rate_cost + desired_profit
    return sale_price

def on_calculate():
    try:
        cost_price = float(cost_price_entry.get())
        if calculation_mode_var.get() == '计算利润':
            sale_price = float(sale_price_entry.get())
            rate_percent = float(rate_percent_entry.get())
            profit = calculate_profit(cost_price, sale_price, rate_percent)
            result_text = f"利润：{profit:.2f} 元"
        else:
            desired_profit = float(profit_entry.get())
            rate_percent = float(rate_percent_entry.get())
            sale_price = calculate_sale_price(cost_price, desired_profit, rate_percent)
            result_text = f"售价：{sale_price:.2f} 元"
        
        result_label.config(text=result_text, fg="blue", font=("黑体", 14))
    except ValueError:
        messagebox.showerror("错误", "请确保所有输入都是有效的数字。")

# 创建主窗口
root = tk.Tk()
root.title("电商计算器")
root.geometry("500x400")

# 设置字体
font_style = ("黑体", 14)

# 创建一个框架来居中所有元素
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# 创建并放置计算模式选择标签和下拉菜单
calculation_mode_var = tk.StringVar(value='计算利润')  # 默认选择

# 在 `refresh_entries` 函数中重新创建和布局所有控件
def refresh_entries(*args):
    for widget in frame.grid_slaves():
        widget.destroy()
    
    # 重新布局计算模式
    mode_label = tk.Label(frame, text="计算模式：", font=font_style)
    mode_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    
    calculation_mode = tk.OptionMenu(frame, calculation_mode_var, '计算利润', '计算售价')
    calculation_mode.grid(row=0, column=1, padx=10, pady=10)
    
    labels = ["成本（元）："]
    if calculation_mode_var.get() == '计算利润':
        labels.append("售价（元）：")
        labels.append("费率（%）：")
    else:
        labels.append("利润（元）：")
        labels.append("费率（%）：")

    entries = []
    for i, label in enumerate(labels, start=1):
        label_widget = tk.Label(frame, text=label, font=font_style)
        label_widget.grid(row=i, column=0, sticky="e", padx=10, pady=10)
        entry = tk.Entry(frame, font=font_style, width=15, justify='center', bg="#d3d3d3")  # 设置深色输入框
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)

    global cost_price_entry, sale_price_entry, profit_entry, rate_percent_entry
    cost_price_entry = entries[0]
    if calculation_mode_var.get() == '计算利润':
        sale_price_entry, rate_percent_entry = entries[1], entries[2]
    else:
        profit_entry, rate_percent_entry = entries[1], entries[2]

    # 创建计算按钮
    calculate_button = tk.Button(frame, text="计算", command=on_calculate, font=font_style, relief=tk.RAISED, bd=3, cursor="hand2", width=20)
    calculate_button.grid(row=len(labels)+1, column=0, columnspan=2, pady=10)

    # 创建结果显示标签
    global result_label
    result_label = tk.Label(frame, text="", font=("黑体", 14), justify="center", fg="blue")
    result_label.grid(row=len(labels)+2, column=0, columnspan=2, sticky="ew", padx=10, pady=20)

# 监听计算模式选择的变化，自动更新输入框
calculation_mode_var.trace('w', refresh_entries)

# 开发者信息
developer_label = tk.Label(root, text="开发者: 布丁文创  |  微信号: tzwl2024  |  版本号: 2.0", font=("黑体", 13), justify="center")
developer_label.pack(side='bottom', pady=10)

# 初次加载时刷新输入框
refresh_entries()

root.mainloop()
