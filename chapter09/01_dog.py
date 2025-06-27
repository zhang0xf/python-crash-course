# 根据约定，在Python中，首字母大写的名称指的是类。这个类定义中的括号是空的，因为我们要从空白(相较于继承)创建这个类。
class Dog():
    """一次模拟小狗的简单尝试""" # 文档字符串，对这个类的功能作了描述
    # __init__()是一个特殊的方法，每当你根据Dog类创建新实例时，Python都会自动运行它。
    # 为何必须在方法定义中包含形参self呢？因为Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。
    def __init__(self, name, age):
        """初始化属性name和age"""
        # 以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量。
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

# Python使用实参'willie'和6调用Dog类中的方法__init__()
# 方法__init__()并未显式地包含return语句，但Python自动返回一个表示这条小狗的实例。
my_dog = Dog('willie',6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is "+str(my_dog.age)+" years old.")

# 调用方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
your_dog = Dog('lucy',3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()