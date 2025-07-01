# 写入文件
filename = 'chapter10/programming.txt'
# 第二个实参('w')告诉Python，我们要以写入模式打开这个文件。打开文件时，可指定读取模式('r')、写入模式('w')、附加模式('a')或让你能够读取和写入文件的模式('r+'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 追加写入
filename = 'chapter10/programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")