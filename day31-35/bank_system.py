# 初始化钱包一万块
bank = [10000]


def init():
    "初始化选项程序，并转向对应的函数"
    print("--------------------")
    print(
        """请输入序号来办理业务：
    1、查询资产
    2、存款
    3、取款
    4、计算贷款
    q、退出"""
    )
    print("--------------------")
    a = input()
    while a != "q":
        if a == "1":
            search()
        elif a == "2":
            save()
        elif a == "3":
            get()
        elif a == "4":
            clD()
        else:
            print("输入的序号错误，请重新输入")
        print()
        a = input("请继续输入功能序号进行功能选择：")
    print("thanks for using! bye!!")


def search():
    print(f"你的资产情况如下：{bank[0]}元")


def save():
    savenum = int(input("请输入你的存款金额："))
    bank[0] += savenum
    print(f"你的钱存好了，原来资产{bank[0]-savenum}，现在资产{bank[0]}")


def get():
    getnum = int(input("请输入你的取款金额："))
    bank[0] -= getnum
    print(f"你的钱取出来了，原来资产{bank[0]+getnum}，现在资产{bank[0]}")


def clD():
    money = int(input("请输入贷款金额："))
    present = int(input("请输入年利率的百分比数："))
    year = int(input("请输入贷款年限："))
    print(f"经过运算，你的贷款应还{money * (1 + present / 100) * year}")


def main():
    init()


if __name__ == "__main__":
    main()
