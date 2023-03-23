s = int(input("请输入年份来判断闰年"))
if (s % 100 == 0 or s % 4 == 0) or s % 400 == 0:
    print(f"{s}年是闰年")
else:
    print(f"{s}年不是闰年")
