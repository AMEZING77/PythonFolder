from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# 创建一个D6
die_1 = Die(6)
die_2 = Die(10)


# 掷几次骰子，并将结果存储在一个列表中
results = []
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]
# for roll_num in range(50_000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
# print(results)

# 分析结果
frequencies = []
min_result = 2
max_result = die_1.num_sides + die_2.num_sides

frequencies = [results.count(value) for value in range(min_result, max_result + 1)]

# for value in range(min_result, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
# print(frequencies)

# 对结果进行可视化
x_values = list(range(min_result, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]
# dtick 是刻度标签的间隔
x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title="Results of rolling one D6 and D10 50_000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
# offline中的filename参数，可以指定生成的html文件名
offline.plot({"data": data, "layout": my_layout}, filename="d6_d10.html")
