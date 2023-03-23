# 判断元素在列表中是否存在
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
search = 5
flag = 1
for i in range(len(s)):
    if s[i] == search:
        print("found")
        flag = 0
        break
if flag:
    print("no")
