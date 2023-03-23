# 检验一个数是否为素数
s = int(input("请输入需要检测是否素数的数"))
flag = 0
for i in range(2, s):
    if s % i == 0:
        print(f"{s}不是素数")
        flag = 1
        break
if flag == 0:
    print(f"{s}是素数")
