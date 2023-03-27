# 二分查找
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = 0
h = len(arr) - 1
s = int(input("请输入需要查找的数："))
ss = 1


def fun(l, h, s):
    global ss
    flag = int((l + h) / 2)
    if arr[flag] == s:
        ss = 0
        print(f"get!flag is {flag+1}")
        return
    elif l == h:
        return
    elif arr[flag] > s:
        h = flag
        fun(l, flag - 1, s)  # 如果flag不减一的话，循环会因为flag=l+h取整的问题，一直死循环
    elif arr[flag] < s:
        l = flag
        fun(flag + 1, h, s)


fun(l, h, s)
if ss:
    print("not found")
