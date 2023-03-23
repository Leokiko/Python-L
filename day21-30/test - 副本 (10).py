# 生成日历

# 引入日历模块
import calendar

# 指定月份
yy = int(input("请输入年："))
mm = int(input("请输入月："))
# 显示日历
print(calendar.month(yy, mm))
