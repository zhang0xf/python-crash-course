def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 位置实参
# 调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。
describe_pet('hamster','harry')
describe_pet('dog','willie')

# 关键字实参
describe_pet(animal_type = 'hamster',pet_name = 'harry')
describe_pet(pet_name = 'harry', animal_type = 'hamster')

# 默认值
def describe_pet(pet_name, animal_type ='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name = 'willie')
describe_pet(pet_name = 'harry', animal_type = 'hamster')