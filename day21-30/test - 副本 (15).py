# 计算n个自然数的立方和
a = int(input("请输入自然数："))
r = 0
for i in range(1, a + 1):
    r += i**3
print(r)
