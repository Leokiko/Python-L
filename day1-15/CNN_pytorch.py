# 导入必要的库
import torch
import torch.nn as nn
import torchvision.datasets as datasets
import torchvision.transforms as transforms

# 定义超参数
num_epochs = 5  # 训练轮数
batch_size = 100  # 批大小
learning_rate = 0.001  # 学习率

# 加载MNIST数据集，将图片转换为张量并归一化到[0,1]区间
train_dataset = datasets.MNIST(
    root="./data", train=True, transform=transforms.ToTensor(), download=True
)

test_dataset = datasets.MNIST(
    root="./data", train=False, transform=transforms.ToTensor()
)

# 创建数据加载器，将数据集分成多个批次进行训练和测试
train_loader = torch.utils.data.DataLoader(
    dataset=train_dataset, batch_size=batch_size, shuffle=True
)

test_loader = torch.utils.data.DataLoader(
    dataset=test_dataset, batch_size=batch_size, shuffle=False
)


# 定义CNN模型，包含两个卷积层和两个全连接层
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # 第一个卷积层，输入通道为1（灰度图），输出通道为16，卷积核大小为5x5，步长为1，填充为2（保持尺寸不变）
        self.conv1 = nn.Conv2d(1, 16, kernel_size=5, stride=1, padding=2)
        # 第一个池化层，使用最大池化，核大小为2x2，步长为2（下采样）
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        # 第二个卷积层，输入通道为16，输出通道为32，卷积核大小为5x5，步长为1，填充为2（保持尺寸不变）
        self.conv2 = nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=2)
        # 第一个全连接层，输入特征维度为7x7x32（经过两次池化后的图片尺寸），输出特征维度为10（类别数）
        self.fc1 = nn.Linear(7 * 7 * 32, 10)

    def forward(self, x):
        # 前向传播函数，定义模型的计算流程
        out = self.conv1(x)  # 卷积操作
        out = torch.relu(out)  # 激活函数
        out = self.pool(out)  # 池化操作
        out = self.conv2(out)  # 卷积操作
        out = torch.relu(out)  # 激活函数
        out = self.pool(out)  # 池化操作

        out = out.reshape(out.size(0), -1)  # 将四维张量展平成二维张量

        out = self.fc1(out)  # 全连接操作

        return out


# 创建CNN模型实例，并移动到GPU上（如果有GPU的话）
model = CNN()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()  # 使用交叉熵损失函数作为分类问题的损失函数
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)  # 使用Adam优化器作为优化算法

# 训练模型

total_step = len(train_loader)  # 计算总的批次数

for epoch in range(num_epochs):  # 遍历每一轮训练
    for i, (images, labels) in enumerate(train_loader):  # 遍历每一个批次的数据
        images = images.to(device)  # 将图片张量移动到GPU上（如果有GPU的话）
        labels = labels.to(device)  # 将标签张量移动到GPU上（如果有GPU的话）

        outputs = model(images)  # 前向传播，得到模型输出
        loss = criterion(outputs, labels)  # 计算损失

        optimizer.zero_grad()  # 清空梯度缓存
        loss.backward()  # 反向传播，计算梯度
        optimizer.step()  # 更新参数

        if (i + 1) % 100 == 0:  # 每隔100个批次打印一次训练信息
            print(
                "Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}".format(
                    epoch + 1, num_epochs, i + 1, total_step, loss.item()
                )
            )

# 测试模型

model.eval()  # 将模型设置为评估模式，关闭dropout等影响测试结果的因素

with torch.no_grad():  # 关闭自动求导，节省内存和计算资源
    correct = 0  # 正确预测的数量
    total = 0  # 总的样本数量

    for images, labels in test_loader:  # 遍历测试集中的每一个批次
        images = images.to(device)  # 将图片张量移动到GPU上（如果有GPU的话）
        labels = labels.to(device)  # 将标签张量移动到GPU上（如果有GPU的话）

        outputs = model(images)  # 前向传播，得到模型输出
        _, predicted = torch.max(outputs.data, 1)  # 得到预测结果，取每一行最大值对应的索引作为类别

        total += labels.size(0)  # 累加总样本数
        correct += (predicted == labels).sum().item()  # 累加正确预测数

    print(
        "Test Accuracy of the model on the 10000 test images: {} %".format(
            100 * correct / total
        )
    )

# 保存模型

torch.save(model.state_dict(), "model.ckpt")
