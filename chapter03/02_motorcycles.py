motorcycles = ['honda','yamaha','suzuki'] 
print(motorcycles)

motorcycles[0] = 'ducati01'
motorcycles.append('ducati02')
motorcycles.insert(0,'ducati03')
print(motorcycles)

# 使用del语句将值从列表中删除后，你就无法再访问它了
del motorcycles[0]
print(motorcycles)

# 方法pop()可删除列表末尾的元素，并让你能够接着使用它
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print(motorcycles)

# 如果你只知道要删除的元素的值，可使用方法remove()
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")