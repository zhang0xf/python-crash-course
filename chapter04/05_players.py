players = ['charles','martina','michael','florence','eli']
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
# 输出名单上的最后三名队员
print(players[-3:])

# 遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())