import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score
import numpy as np
import torch.utils
import torch.utils.data
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F

#classification about picture
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

num_epoch = 1
batch_size = 10
learning_rate = 0.001

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, transform=transform, download=True)
test_dataset = torchvision.datasets.CIFAR10(root='./data', train=False, transform=transform)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

dataiter = iter(train_loader)
images, labels = next(dataiter)

class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5) #input channel(3 เพราะCIFAR10 มี3 channel ในหลักการของ cnn), output channel(6), kernel(5) ไอ้ที่เหลือนี่ optimize เอง   
        #(หากทำ projects เเล้วจะหา channel ของ your picture เเนะนำใช้ openCV, chatgpt บอกมา)
        self.pool = nn.MaxPool2d(2, 2) #ลดขนาดเหลือ 2*2 (มันจะเอาขนาดรูปภาพ มาหารครึ่ง เช่น 32, 32 > 16, 16)
        self.conv2 = nn.Conv2d(6, 16, 5) #รอบนี้ ช่องเเรก = output channel, ที่เหลือ optimize เองเหมือนเดิม
        self.fc1 = nn.Linear(16*5*5, 120) #16*5*5 is fixed, 16 is from output channel in conv2  and เเละ5 มาจากการหักจาก conv2 เหลือ10 เเละหักจาก pool เหลือ5 (เเรกเริ่มเดิมทีมัน32, 32) (ถ้าอยากรู้ว่ามันหักยังไง ไปดูสูตร)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10) #10 is fixed (because of 10 classes)
        # 120 and 84 are depends on you

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16*5*5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = ConvNet().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

n_total_steps = len(train_loader)
for epoch in range(num_epoch):
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels =  labels.to(device)

        outputs = model(images)
        loss =  criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (i+1) % 2000 == 0 :
            print(f"epoch{epoch+1}/{num_epoch}, step{i+1}/{n_total_steps}, loss : {loss.item():.4f}")
print("finished training")

with torch.no_grad():
    n_correct = 0
    n_samples = 0
    scikitAcc = 0
    n_class_correct = [0 for i in range(10)]
    n_class_samples = [0 for i in range(10)]
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)
        outputs = model(images)

        _, prediction = torch.max(outputs, 1)
        n_samples += labels.size(0)
        n_correct += (prediction == labels).sum().item()

        scikitAcc += accuracy_score(prediction, labels)

        for i in range(batch_size):
            label = labels[i]
            pred = prediction[i]
            if (label == pred):
                n_class_correct[label] += 1
            n_class_samples[label] += 1

    for i in range(10):
        acc = 100 * n_class_correct[i] / n_class_samples[i]
        print(f"accurate of {classes[i]}: {acc}%")

    acc = 100 * n_correct/n_samples
    scikitAcc = scikitAcc/(len(test_loader))
    print(f"model accurate by self : {acc}%")
    print(f"model accurate by scikit {scikitAcc}")
    print(len(test_loader), len(train_loader))