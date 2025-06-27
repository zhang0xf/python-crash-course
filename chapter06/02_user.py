user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

# 遍历字典
for key,value in user_0.items():
    print("\nKey:" + key)
    print("Value:" + value)

# 遍历字典中的所有键
favorite_languages = {
   'jen':'python',
   'sarah':'c',
   'edward':'ruby',
   'phil':'python',
}

friends = ['phil','sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("  Hi " + name.title() + 
            ",I see your favorite language is " + 
            favorite_languages[name].title() + "!")

# 方法keys()并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键
if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!")

# 排序键
for name in sorted(favorite_languages.keys()):
    print(name.title()+",thank you for taking the poll.")

# 字典值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 为剔除重复项，可使用集合(set)。集合类似于列表，但每个元素都必须是独一无二的
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())