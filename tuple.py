# 元组的最大特点是不可以被修改
# 元组创建方式：
a = (1,2,3)
b = a
# 原来的元组 a 没有被修改，只是 b 重新创建了有个元组；
b = (4,5,6) 
print(a)
print(b)

# 第二种元组创建方式，python 会自动转化为元组类型
c = 1,2,3

# 访问元组中的元素
c[0]
print(c[0])

# 元组切片 前闭后开区间
c[0:2]
print(c[0:2])

# 也可以用负数，表示从尾部倒数查询
c[-3:-1]
print(c[-3:-1])