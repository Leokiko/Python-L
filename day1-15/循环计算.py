# # 交换两个变量的值
# a = 1
# b = 2
# # a, b = b, a
# # print(a, b)
# c = a
# a = b
# b = c
# print(a, b)


# # 求最大公约数
# a = 90
# b = 45
# m = 1
# c = max(a, b)
# d = min(a, b)
# re = 0
# e = 1
# while e <= d:
#     if c % e == 0 and d % e == 0:
#         re = e
#     e += 1
# print(re)


# # 输入n，输出不大于n的斐波那契数
# n = 15
# a, b = 0, 1
# # while a < n:
# #     print(a)
# #     a, b = b, a + b
# while a < n:
#     print(a, end=",")
#     a, b = b, a + b


# # 计算水费
# n = float(input("请输入用水量"))
# re = 0
# if n <= 15:
#     re = 4 * n / 3
# else:
#     re = 2.5 * n - 17.5
# print(re)


# # 阶梯电价
# x = int(input("请输入用电量"))
# re = 0
# if x <= 2760:
#     re = 0.538 * x
# elif x <= 4800:
#     re = 2760 * 0.538 + 0.588 * (x - 2760)
# else:
#     re = 2760 * 0.538 + 0.588 * 2040 + 0.838 * (x - 4800)
# print(re)


# # 能否构成三角形，输入三角形的三条边，判断能否构成三角形，能则yes，否则no
# a, b, c = map(int, input("请输入三角形的三条边，之间使用空格隔开").split())
# M = max(a, b, c)
# m = min(a, b, c)
# re = M - m
# no = 0
# if M == a or m == a:
#     if M == b or m == b:
#         no = c
#     else:
#         no = b
# else:
#     no = a
# if re < no:
#     print("yes")
# else:
#     print("no")


# # 判断闰年
# y = int(input("请输入年份"))
# if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
#     print(f"{y}是闰年")
# else:
#     print(f"{y}不是闰年")


# 计算油费：现在90号汽油6.95元/升、93号汽油7.44元/升、97号汽油7.93元/升。
# 为吸引顾客，某自动加油站推出了“自助服务”和“协助服务”两个服务等级，分别可得到5%和3%的折扣。 本题要求编写程序，根据输入顾客的加油量a，汽油品种b（90、93或97）和服务类型c（m-自助，e-协助），计算输出应付款
a, b, c = map(str, input().split())
re = 0
if b == "90":
    re = int(a) * 6.95
elif b == "93":
    re = int(a) * 7.44
else:
    re = int(a) * 7.93
if c == "m":
    re *= 0.95
else:
    re *= 0.97
print(re)
