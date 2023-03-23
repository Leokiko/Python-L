# 计算最小公倍数
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
c = max(a, b)
r = c
while True:
    if r % a == r % b == 0:
        print(f"{a}和{b}的最小公倍数是{r}")
        break
    r += 1
