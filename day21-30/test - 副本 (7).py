# 实现计算器
def plus(a, b):
    return a + b


def replus(a, b):
    return a - b


def chen(a, b):
    return a * b


def chu(a, b):
    return a / b


a, b = map(int, input("请输入两个数").split())
r = int(input("请选择计算方法1加2减3乘4除"))
if r == 1:
    print(f"计算结果为{plus(a,b)}")
elif r == 2:
    print(f"计算结果为{replus(a,b)}")
elif r == 3:
    print(f"计算结果为{chen(a,b)}")
elif r == 4:
    print(f"计算结果为{chu(a,b)}")
else:
    print("计算方法选择错误")
