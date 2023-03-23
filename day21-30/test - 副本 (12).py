# 计算最大公约数

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
a = max(num1, num2)
b = min(num1, num2)
# 方法1，直接计算
r = 1
for i in range(2, b + 1):
    if a % i == 0 and b % i == 0:
        r = i
print(r)


# 方法2，使用函数来进行计算
def maxca(a, b):
    a1 = max(a, b)
    b1 = min(a, b)
    r = 1
    for i in range(2, b + 1):
        if a % i == 0 and b % i == 0:
            r = i
    print(r)


maxca(num1, num2)
