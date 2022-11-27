import copy

# 浅拷贝
l1 = [1, 2, 3, [4, 5]]
l2 = copy.copy(l1)
l1.append(6)
print(l1)
print(l2)
# l1[3] 为可变变量
l1[3].append(666)
print(l1)
print(l2)

# 深拷贝
l4 = [1, 2, 3, [4, 5]]
l5 = copy.deepcopy(l4)
l4[3].append(666)
print(l4)
print(l5)

# 不可变变量 int float string
x1 = (1, 2, 3)
x2 = x1
x3 = copy.copy(x1)
x4 = copy.deepcopy(x1)
x1 = (5, 6, 7)
print(x1)
print(x2)
print(x3)
print(x4)
