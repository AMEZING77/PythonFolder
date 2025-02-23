import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x**2 for x in x_values]


plt.style.use("seaborn-v0_8-darkgrid")
fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
# c=y_values 是色值，cmap=plt.cm.Blues 是颜色映射，s=10 是点的大小
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置图标题目和坐标轴标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=18)
ax.set_ylabel("值的平方", fontsize=18)

ax.axis([-1, 6, 0, 30])
# 设置刻度标记的大小
ax.tick_params(axis="both", which="major", labelsize=14)

# 第一个参数是文件名，第二个参数是裁剪掉空白区域
# tight 裁剪掉空白区域
plt.savefig("squares_plot.png", bbox_inches="tight")
# show之后会清空图表，需要在之前保存fig
plt.show()
