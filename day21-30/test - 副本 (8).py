# 输出指定范围内的素数
a, b = map(int, input("请输入下界与上界").split())
r = 1
for i in range(a, b + 1):
    flag = 1
    for j in range(2, i):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        print(f"从{a}到{b}里的第{r}个素数是{i}")
        r += 1
