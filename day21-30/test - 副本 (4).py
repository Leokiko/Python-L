# 输出阶乘结果
s = int(input("输入斐波那契数n"))
r = 1
if s < 0:
    print("负数没有阶乘")
elif s == 0:
    print("0的阶乘为1")
else:
    for i in range(1, s + 1):
        r *= i
    print(r)
