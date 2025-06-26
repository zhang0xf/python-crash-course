# Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
# 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)