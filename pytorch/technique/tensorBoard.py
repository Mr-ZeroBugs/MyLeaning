import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
from sklearn.metrics import accuracy_score
import sys
#to open tensorboard we have to type "tensorboard --logdir=(any name)" in powershell (1) (i recommend powershell cuz i tried in another as cmd but its failed)
from torch.utils.tensorboard import SummaryWriter #import this after running tensorboard(2)

#(this is code from model nn.py)
#then (3)
writer = SummaryWriter("test/Mnist(pr curve)") #up to you

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')   

#hyper params
input_size = 784 #28*28
hidden_size = 500
num_classes = 10 # 0 - 9 from mnist
num_epochs = 1
batch_size = 64
learning_rate = 0.001

#mnist
train_dataset = torchvision.datasets.MNIST('./data', transform=transforms.ToTensor(), train=True, download=True) #download = True ถ้ายังไม่เคย
test_dataset = torchvision.datasets.MNIST('./data', transform=transforms.ToTensor(), train=False, download=True)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

examples =  iter(train_loader) #ต้องใช้ iter เเละเข้าถึงผ่าน next ไม่งั้นไม่ได้
samples, labels = next(examples)

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(samples[i][0], cmap='gray')
#plt.show()
img_grid = torchvision.utils.make_grid(samples) #step4(Not required) add images to tensorboard, use this instead of plt.show()
writer.add_image("mnist_grid(fixed to 8*8(batch = 64))", img_grid)

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

#tensorboard step 5 (Not required)
writer.add_graph(model, samples.reshape(-1, 28*28)) # add graph to tensorboard
writer.close()

#training loop
n_total_steps = len(train_loader)
runningloss = 0.0
runningcorrect = 0.0
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

        runningloss += loss.item()
        _, prediction = torch.max(outputs.data, 1)
        runningcorrect += (prediction == labels).sum().item()


        if (i+1) % 100 == 0:
            print(f"epoch {epoch+1}/{num_epochs}, step{i+1}/{n_total_steps}, loss = {loss.item():.4f}")
            writer.add_scalar('training loss', runningloss/100, epoch*n_total_steps + i)
            writer.add_scalar('accuracy', runningcorrect/100, epoch*n_total_steps + i)
            runningloss = 0.0
            runningcorrect = 0 #it's just loss,acc "of trainning" not the real loss,acc
            #the benefit of seeing training acc,loss are that you can see the model trends
#test
labels = [] #เพิ่มมาใหม่เพื่อ add to tensorboard
preds = []
with torch.no_grad():
    n_correct = 0
    n_samples = 0
    scikit = 0
    for images, labels1 in test_loader:
        images = images.reshape(-1, 28*28).to(device)
        labels1 = labels1.to(device)

        outputs = model(images) 
        _, prediction = torch.max(outputs.data, 1) 
        n_samples += labels1.shape[0]
        n_correct += (prediction == labels1).sum().item()

        #step of recall curve
        class_predic = [F.softmax(output, dim=0)for output in outputs] #ที่เราทำเป็น softmax ทั้งๆที่เราใช้ cross ไปเเล้ว ในกรณีนี้เพราะเราต้องการค่าความน่าจะเป็นจาก softmax
        preds.append(class_predic)
        labels.append(labels1)

        scikit += (accuracy_score(prediction, labels1))

    #step of recall curve
    labels = torch.cat(labels) #.cat มันจะนำข้อมูลมาต่อกัน ่ เช่น 1,2,3 + 4,5,6 = 1,2,3,4,5,6
    preds = torch.cat([torch.stack(batch)for batch in preds])

    acc = 100.0 * n_correct /  n_samples
    accByScikit = scikit/len(test_loader) 
    print(acc, "accuracy by doing it your self")
    print(accByScikit, "accuracy by scikit")
    print(len(train_loader), len(test_loader)) 

#recall curve to tensorboard
    classes = range(10)
    for i in classes:
        labesl_i = labels == i
        preds_i = preds[:, i]
        writer.add_pr_curve(str(i), labesl_i, preds_i, global_step=0, weights=1) #recall curve
        writer.close()

#afterall we open new powershell and type python "your path to this file" and run
#if u want to reset tensorboard web then u can do last step again ^

"redata in tensorboard"
#if you want to reset data in tensorboard, you have to close tensorboard, powershell and open it again
#then you type. tensorboard log/dir = (new name)
#be careful, if u use old name it'll give u old data

"add data to tensorboard"
#if you want to add some new data to board
#you just modify your code and then Rename the writer = Summa(oldfolder/newname) like this