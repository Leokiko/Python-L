# 使用Python在控制台实现一个通讯录管理系统
def main():
    # 1.定义一个字典，用于存储姓名和电话号码
    contacts = {}
    while True:
        # 2.显示功能菜单
        show_menu()
        # 3.获取用户输入的功能选项
        menu_option = input("请输入功能选项：")
        # 4.根据用户输入的功能选项，执行不同的功能
        if menu_option == "1":
            # 添加姓名和电话号码
            add(contacts)
        elif menu_option == "2":
            # 删除姓名和电话号码
            delete(contacts)
        elif menu_option == "3":
            # 修改姓名和电话号码
            modify(contacts)
        elif menu_option == "4":
            # 查询姓名和电话号码
            search(contacts)
        elif menu_option == "5":
            # 显示所有联系人的姓名和电话号码
            show_all(contacts)
        elif menu_option == "6":
            # 退出系统
            break
        else:
            # 提示用户输入有误
            print("您输入的功能选项有误，请重新输入！")


def show_menu():
    """显示功能菜单"""
    print("*" * 50)
    print("欢迎使用通讯录管理系统 V1.0")
    print("1.添加姓名和电话号码")
    print("2.删除姓名和电话号码")
    print("3.修改姓名和电话号码")
    print("4.查询姓名和电话号码")
    print("5.显示所有联系人的姓名和电话号码")
    print("6.退出系统")
    print("*" * 50)


def add(contacts):
    """添加姓名和电话号码"""
    name = input("请输入姓名：")
    phone = input("请输入电话号码：")
    contacts[name] = phone
    print("添加成功！")


def delete(contacts):
    """删除姓名和电话号码"""
    name = input("请输入要删除的姓名：")
    if name in contacts:
        del contacts[name]
        print("删除成功！")
    else:
        print("您输入的姓名不存在！")


def modify(contacts):
    """修改姓名和电话号码"""
    name = input("请输入要修改的姓名：")
    if name in contacts:
        phone = input("请输入新的电话号码：")
        contacts[name] = phone
        print("修改成功！")
    else:
        print("您输入的姓名不存在！")


def search(contacts):
    """查询姓名和电话号码"""
    name = input("请输入要查询的姓名：")
    if name in contacts:
        print("查询结果如下：")
        print("姓名：%s，电话号码：%s" % (name, contacts[name]))
    else:
        print("您输入的姓名不存在！")


def show_all(contacts):
    """显示所有联系人的姓名和电话号码"""
    print("所有联系人的姓名和电话号码如下：")
    print("姓名\t\t电话号码")
    for name, phone in contacts.items():
        print("%s\t\t%s" % (name, phone))


if __name__ == "__main__":
    main()
