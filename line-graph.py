import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 全局设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是黑体的字体名称
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 接下来的代码与上面相同，不再需要指定 fontproperties



# 年份、GDP和增长率数据
years = [2019, 2020, 2021, 2022, 2023]
gdp = [2100, 2200, 2300, 2500, 2700]
growth_rate = [6.5, 5.8, 6.2, 7.1, 7.5]

# 创建折线图
fig, ax1 = plt.subplots(figsize=(10, 5))  # 设置图形的大小

# 绘制GDP折线图
color = 'tab:blue'
ax1.set_xlabel('年份')
ax1.set_ylabel('GDP (亿元)', color=color)
ax1.plot(years, gdp, marker='o', label='GDP (亿元)', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# 实例化第二个Y轴
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('增长率 (%)', color=color)  
ax2.plot(years, growth_rate, marker='s', label='增长率 (%)', color=color)
ax2.tick_params(axis='y', labelcolor=color)

# 添加图例
fig.tight_layout()  # 调整布局以适应图例
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), bbox_transform=ax1.transAxes)
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9), bbox_transform=ax1.transAxes)

# 添加标题
plt.title('揭阳市近五年GDP及增长率')

# 显示网格
ax1.grid(True)

# 显示图形
plt.show()