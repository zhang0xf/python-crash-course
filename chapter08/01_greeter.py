# 使用关键字def来告诉Python你要定义一个函数。这是函数定义，向Python指出了函数名，还可能在括号内指出函数为完成其任务需要什么样的信息。
def greet_user():
    # 文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。
    """显示简单的问候语"""
    print("Hello!")

# 函数调用
greet_user() 

# 向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello," + username.title() + "!")

greet_user('jesse')