from urllib.request import urlopen
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
filename_urllib = 'project/data_visualization/btc_close_2017_urllib.json'

response = urlopen(json_url)
# 读取数据
req = response.read()
# 将数据写入文件
with open(filename_urllib,'wb') as f:
    f.write(req)
# 加载json格式
file_urllib = json.loads(req)
print(file_urllib)