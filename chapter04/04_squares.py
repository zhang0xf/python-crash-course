squares = []
for value in range(1,11):
    # 在Python中，两个星号(**)表示乘方运算
    squares.append(value**2)
print(squares)

# 使用列表解析创建平方数列表
# 定义一个表达式(value**2)，用于生成你要存储到列表中的值
squares = [value**2 for value in range(1,11)]
print(squares)