# # 复数可以直接使用“数+数j”的形式来创建，也可以使用complex函数来进行创建
# a = 1 + 1j
# print(a, type(a))
# b = complex(2, 2)
# print(a + b)
# print(a.real, a.imag, abs(a), a.conjugate())  # 一些常用函数


# # 输出月份的缩写
# monthName = "JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEV"
# a = int(input("输入数字表示的月份"))
# print(monthName[a - 1 : a + 2])


# # 带符号的温度输入，识别输入的是华氏温度还是摄氏温度,并进行温度的净值转换
# tempture = input("请输入温度大小，并以C或F来代表温度类型")
# if tempture[len(tempture) - 1] == "C":
#     print(f"这是摄氏温度，温度值为{tempture[0:-1]}，转化为华氏温度值为{int(tempture[0:-1])*1.8+32}")
# else:
#     print(f"这是华氏温度，温度值为{tempture[0:-1]}")

# #字符串切片slice
# a = "123456789"
# print(a[:])
# print(a[:-2])
# print(a[::-2])
# print(a[::1])
# print(a[::2])
# print(a[::3])
# print(a[::-1])


# # 某月份所属的季节，根据所输入的月份，打印月份所属的时间，输入非法时，提示非法
# monthNum = int(input("请输入月份的数字"))
# if monthNum > 0 and monthNum < 4:
#     print("春季")
# elif monthNum > 3 and monthNum < 7:
#     print("夏季")
# elif monthNum > 6 and monthNum < 9:
#     print("秋季")
# elif monthNum > 8 and monthNum < 13:
#     print("冬季")
# else:
#     print("输入不合法")
