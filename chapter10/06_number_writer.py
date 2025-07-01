# 使用JSON来存储数据
import json

numbers = [2,3,5,7,11,13]
filename = 'chapter10/numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)