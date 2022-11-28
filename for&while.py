# for 循环(可迭代对象)使用，使用确定循环次数
for i in range(10):
    if i == 3:
        # 结束本轮循环
        continue
    if i == 6:
        # 结束整个循环
        break
    print(i)

# while 循环使用 适用不确定循环次数
i = 0
while i < 20:
    print(i)
    i += 1
