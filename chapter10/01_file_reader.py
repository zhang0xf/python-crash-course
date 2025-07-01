# 关键字with在不再需要访问文件后将其关闭
with open('chapter10/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 逐行读取
filename = 'chapter10/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
filename = 'chapter10/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())