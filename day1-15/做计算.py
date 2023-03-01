# # 格式化输入输出
# # 使用格式化字符格式化
# a = 0.123456789
# b = 0.987654321
# # 标志符进行格式化输出
# print("%f|%f" % (a, b))

# # 使用.format格式化
# # 使用名称占位符
# s1 = "{age} {name}".format(age=18, name="hangman")
# print(s1)  # 18 hangman
# # 使用序号占位符，为空默认从左到右01234.。。【这里注意b是在前面被显示的】
# s2 = "show1{1} show2{0}".format(a, b)
# print(s2)  # show10.987654321 show20.123456789
# # 也可以混合使用
# s3 = "show1{} show2{name} show3{}".format(b, a, name="s3")
# print(s3)  # show10.987654321 show2s3 show30.123456789

# # 使用f字符串格式化
# s4 = f"show1 is {a},show2 is {b:.2f},show3 is {a:.3%}"
# print(s4)  # show1 is 0.123456789,show2 is 0.99,show3 is 12.346%


# #计算圆的面积
# radius = float(input("请输入圆的半径："))
# area = 3.14159 * radius**2
# print(f"半径为{radius:.2f}的圆的面积是：{area:.2f}")


# # 给出一天内两个分别用小时和分钟表示的时间，计算两个时间的差，结果表示为小时和分钟
# # 比如输入：
# # 11 30
# # 12 45
# # 表示11点30分和12点45分，输出：
# # 1 15
# a = input("请输入第一个时间的小时和分钟数，以空格隔开，并以回车结束")
# b = input("请输入第二个时间的小时和分钟数，以空格隔开，并以回车结束")
# print(f"a{a} b{b} typea{type(a)} typeb{type(b)}")
# c = a.split()
# d = b.split()
# print(f"a{a} b{b} typea{type(a)} typeb{type(b)}")
# m = int(d[1]) - int(c[1])
# if m < 0:
#     m = m + 60
#     h = int(d[0]) - int(c[0]) - 1
# else:
#     h = int(d[0]) - int(c[0])
# print(f"两个时间差为{h}小时{m}分钟")


# # 计算平均数
# # 输入数据为很多行，每一行一个非负整数
# # 最后一行为-1，表示输入结束，这个-1不是有效数据的一部分
# s = 0
# n = 0
# while 1:
#     a = input("请输入数据，以-1结束")
#     if a == "-1":
#         break
#     s += int(a)
#     n += 1
# print(int(s / n))


# # 本题要求编写程序，打印一个高度为 3 的，由 * 组成的方形图案
# print(
#     """
# * * *
# * * *
# * * *
# """
# )


# 本题要求编写程序，计算该公式的答案：99*12+25*3
print(99 * 12 + 25 * 3)
