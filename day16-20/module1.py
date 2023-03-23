def bim(person, height, weight):
    "根据身高体重算出bmi"
    bim = weight / (height**2)
    print(f"{person} 的bim是：{bim}")


a = 10

if __name__ == "main":
    bim("san", 20, 30)
