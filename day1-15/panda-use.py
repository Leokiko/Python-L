import pandas as pd

# df = pd.read_excel("https://www.gairuo.com/file/data/dataset/team.xlsx")
# df = pd.read_excel(r"D:\GitHub-Clone\Python-L\day1-15\team.xlsx")
df = pd.read_excel("D:/GitHub-Clone/Python-L/day1-15/team.xlsx")

print(df.head(50))
print(df.tail())
print(df.sample())

print(df.shape)  # (100, 6) 查看行数和列数
df.info()  # 查看索引、数据类型和内存信息
print(df.describe())  # 查看数值型列的汇总统计
print(df.dtypes)  # 查看各字段类型
print(df.axes)  # 显示数据行和列名
print(df.columns)  # 列名
