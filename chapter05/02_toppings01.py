requested_topping = 'mushrooms'
# 你编写的大多数条件表达式都检查两个值是否相等，但有时候检查两个值是否不等的效率更高。
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 要判断特定的值是否已包含在列表中，可使用关键字in。
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms'in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni'in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese'in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# _
if 'mushrooms'in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni'in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese'in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# _
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


# 判断列表不为空
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# _
available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry,we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")