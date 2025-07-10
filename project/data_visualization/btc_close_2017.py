import json
import pygal
import math
from itertools import groupby

filename = 'project/data_visualization/data/btc_close_2017.json'

with open(filename) as f:
    btc_data = json.load(f)

# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
closes = []

# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    dates.append(date)
    month = int(btc_dict['month'])
    months.append(month)
    week = int(btc_dict['week'])
    weeks.append(week)
    weekday = btc_dict['weekday']
    weekdays.append(weekday)
    close = int(float(btc_dict['close']))
    closes.append(close)
    print("{} is month {} week {},{},the close price is {} RMB".format(date,month,week,weekday,close))

# x_label_rotation=20让x轴上的日期标签顺时针旋转20°
# show_minor_x_labels=False则告诉图形不用显示所有的x轴标签
line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title = '收盘价(¥)'
line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次,这样x轴就不会显得非常拥挤了
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in closes] # 对数变换(以10为底),用对数变换剔除非线性趋势之后，整体上涨的趋势更接近线性增长
line_chart.add('收盘价',close_log)
line_chart.render_to_file('project/data_visualization/收盘价折线图(¥).svg')

def draw_line(x_data,y_data,title,y_legend):
    xy_map = []
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
        y_list = [v for _,v in y]
        xy_map.append([x,sum(y_list) / len(y_list)])
    x_unique,y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file('project/data_visualization/'+title+'.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month],closes[:idx_month],'收盘价月日均值(¥)','月日均值')

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week],closes[1:idx_week],'收盘价周日均值(¥)','周日均值')

idx_week = dates.index('2017-12-11')
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int = [wd.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int,closes[1:idx_week],'收盘价星期均值(¥)','星期均值')
line_chart_weekday.x_labels = ['周一','周二','周三','周四','周五','周六','周日']
line_chart_weekday.render_to_file('project/data_visualization/收盘价星期均值(¥).svg')

# 每个SVG文件打开之后都是独立的页面。如果能够将它们整合在一起，就可以很方便地进行长期管理、监测和分析
# 另外，新的图表也可以十分方便地加入进来，这样就形成了一个数据仪表盘(dashboard)
with open('project/data_visualization/收盘价Dashboard.html','w',encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            'project/data_visualization/收盘价折线图(¥).svg',
            'project/data_visualization/收盘价对数变换折线图(¥).svg',
            'project/data_visualization/收盘价月日均值(¥).svg',
            'project/data_visualization/收盘价周日均值(¥).svg',
            'project/data_visualization/收盘价星期均值(¥).svg']:
        html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')