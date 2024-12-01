import matplotlib.pyplot as plt

# 全局设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是黑体的字体名称
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 产业类别和贡献比例数据
industries = ['制造业', '农业', '服务业']
contributions = [45, 20, 35]

# 创建饼状图
plt.figure(figsize=(8, 8))  # 设置图形的大小

# 绘制饼状图
plt.pie(contributions, labels=industries, autopct='%1.1f%%', startangle=140)

# 添加标题
plt.title('揭阳市三大产业对GDP的贡献比例饼图')

# 显示图形
plt.show()