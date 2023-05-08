# 导入必要的库
import torch
from PIL import Image
from torchvision import transforms

# 定义类别标签
classes = ["cat", "dog"]

# 加载模型
model = torch.load("D:\GitHub-Clone\Python-L\model.pth")
print(model)
# 设置模型为评估模式
model.eval()

# 打开图片文件
image = Image.open("test1.jpg")

# 将图片转换为张量，并进行归一化和裁剪等预处理操作
transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ]
)
input = transform(image)
input = input.unsqueeze(0)  # 增加一个批次维度

# 将张量传递给模型，得到输出
output = model(input)

# 计算输出的最大值和对应的索引
_, index = torch.max(output, 1)

# 根据索引得到类别标签
label = classes[index.item()]

# 打印结果
print("The image is predicted as:", label)
