"""
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。

C、D、E依次醒来，也按同样的方法拿鱼。

问他们至少捕了多少条鱼?
"""
e = 6
d = e * 5 + 1
c = d * 5 + 1
b = c * 5 + 1
a = b * 5 + 1
print(a)
# 输出3906，是不对的，因为鱼是一个整的，每次分堆堆，都是int，不能有小数


# 正确代码
# def ca(i):
#     if (i - 1) % 5 == 0:
#         print((i - 1) / 5 * 4)
#         return (i - 1) / 5 * 4
#     else:
#         return None


# j = 300
# while True:
#     if (ca(ca(ca(ca(ca(j)))))) % 1 == 0:
#         break
#     j += 1
# print(f"最少捕了{j}条鱼")
# ca(ca(ca(ca(ca(3000)))))


i = 1


def ca(i):
    if (i - 1) % 5 == 0 and i != 0:
        return (i - 1) / 5 * 4
    else:
        return None  # 这里return false也可以


while True:
    if ca(i):
        if ca(ca(i)):
            if ca(ca(ca(i))):
                if ca(ca(ca(ca(i)))):
                    if ca(ca(ca(ca(ca(i))))):
                        print(i)
                        break
    i += 1
