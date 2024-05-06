import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torchvision
import torchvision.transforms as transforms
from sklearn.metrics import accuracy_score

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')   

#hyper params
input_size = 784 #28*28
hidden_size = 128
num_classes = 10 # 0 - 9 from mnist
num_epochs = 5
batch_size = 100
learning_rate = 0.0001

#mnist
train_dataset = torchvision.datasets.MNIST('./data', transform=transforms.ToTensor(), train=True) #download = True ถ้ายังไม่เคย
test_dataset = torchvision.datasets.MNIST('./data', transform=transforms.ToTensor(), train=False)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

examples =  iter(train_loader) #ต้องใช้ iter เเละเข้าถึงผ่าน next ไม่งั้นไม่ได้
samples, labels = next(examples)
print(samples.shape, labels.shape)

#for i in range(6):
    #plt.subplot(2, 3, i+1)
    #plt.imshow(samples[i][0], cmap='gray')
#plt.show()

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self ).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()  
        self.l2  = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        return out

model = NeuralNet(input_size, hidden_size, num_classes).to(device)

criterion = nn.CrossEntropyLoss()
optimizer =  torch.optim.Adam(model.parameters(), lr=learning_rate)

#training loop
n_total_steps = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        images = images.reshape(-1, 28*28).to(device)
        labels = labels.to(device)

        #forward
        outputs = model(images)
        loss = criterion(outputs, labels)

        #backward
        loss.backward()
        optimizer.step()

        if (i+1) % 100 == 0:
            print(f"epoch {epoch+1}/{num_epochs}, step{i+1}/{n_total_steps}, loss = {loss.item():.4f}")
        
#test
with torch.no_grad():
    n_correct = 0
    n_samples = 0
    for images, labels in test_loader:
        images = images.reshape(-1, 28*28).to(device)
        labels = labels.to(device)
        outputs = model(images) #คือมันจะเก็บความเป็นไปได้เอาไว้มากมาย matrixขนาด rows = batch_size, columns = num_classes 0-9 
        _, prediction = torch.max(outputs, 1) #ทีนี้เราก้นำ .max มาดึง classes ที่มีเเนวโน้มเป็นไปได้มากที่่สุดออกมา
        n_samples += labels.shape[0]
        n_correct += (prediction == labels).sum().item() 

    acc = 100.0 * n_correct / n_samples
    print(acc)


