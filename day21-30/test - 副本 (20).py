a = [1, 2, 3, 4, 5, 6]
b = 1


def fun():
    a[0] = 999
    # a = [111, 222]  这句话直接就是报错的
    b = 2
    print(a, b)


def fun1():
    global b
    b = 3
    print(b)


fun()
print(a, b)
fun1()
print(a, b)
