# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        if j == i:
            print(f"{j}x{i}={i*j}", end="")
        else:
            print(f"{j}x{i}={i*j}", end=" ")
    print()
