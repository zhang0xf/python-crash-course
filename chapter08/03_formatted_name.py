# 在函数中，可使用return语句将值返回到调用函数的代码行。
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi','hendrix')
print(musician)

# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name = ''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + '' + middle_name + '' + last_name
    else:
        full_name = first_name + '' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)