import matplotlib.pyplot as plt
import numpy as np

# 全局设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是黑体的字体名称
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 城市、经济增长速度和产业结构数据
cities = ['揭阳市', '汕头市', '潮州市', '梅州市']
growth_rates = [7.5, 6.8, 5.9, 6.2]
industry_structures = [
    [45, 20, 35],  # 揭阳市
    [40, 25, 35],  # 汕头市
    [35, 30, 35],  # 潮州市
    [40, 20, 40]   # 梅州市
]
industries = ['制造业', '农业', '服务业']  # 定义产业类别

# 设置柱状图宽度和位置
bar_width = 0.2
x = np.arange(len(cities))

# 创建图形和轴对象
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制经济增长速度条形柱状图
ax1.bar(x, growth_rates, bar_width, label='经济增长速度（%）', color='grey')
for i, rate in enumerate(growth_rates):  # 在条形柱状图的每个柱子上方显示数值
    ax1.text(x[i], rate + 0.5, f'{rate}%', ha='center', va='bottom', color='grey')

ax1.set_xlabel('城市')
ax1.set_ylabel('经济增长速度（%）', color='grey')
ax1.tick_params(axis='y', labelcolor='grey')
ax1.set_xticks(x)
ax1.set_xticklabels(cities)

# 实例化第二个Y轴
ax2 = ax1.twinx()

# 绘制产业结构柱状图，并在柱子上方显示数值
for i, percentages_city in enumerate(industry_structures):
    bottom = 0
    for j, p in enumerate(percentages_city):
        ax2.bar(x[i] + bar_width, p, bar_width, label=f'{cities[i]} {industries[j]}（%）', color=['blue', 'green', 'orange'][j], bottom=bottom)
        # 在柱子上方显示数值
        ax2.text(x[i] + bar_width, p + 0.5, f'{p}%', ha='center', va='bottom')
        bottom += p

ax2.set_ylabel('产业结构（%）', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# 添加图例
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# 添加标题
plt.title('各城市经济增长速度及产业结构')

# 显示图形
plt.show()