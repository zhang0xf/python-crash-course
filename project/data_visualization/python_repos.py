import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
# 执行API调用并存储响应
# 大多数API都存在速率限制，即你在特定时间内可执行的请求数存在限制

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)
# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])
# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))
# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nSelected information about first repository:")
# print('Name:',repo_dict['name'])
# print('Owner:',repo_dict['owner']['login'])
# print('Stars:',repo_dict['stargazers_count'])
# print('Repository:',repo_dict['html_url'])
# print('Created:',repo_dict['created_at'])
# print('Updated:',repo_dict['updated_at'])
# print('Description:',repo_dict['description'])

# 研究有关仓库的信息
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'], # 在图表中添加可单击的链接
        }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('project/data_visualization/python_repos.svg')