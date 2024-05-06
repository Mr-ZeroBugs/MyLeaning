import numpy as np
import torch
import math
from torch.utils.data import Dataset, DataLoader
import torchvision

class WineDataset(Dataset):

    def __init__(self, transform=None):
        xy = np.loadtxt('wine.csv',delimiter=',', dtype=np.float32, skiprows=1) #skip line1 cuz it's header
        self.x = (xy[:, 1:]) #ที่ต้องใส่ torch.fromnumpy เพื่อให้ torch มันสร้าง tensor ให้อะนะ
        self.y = (xy[:, [0]])
        #เพราะเลือกใช้ numpy.read มันไม่ได้มีfunc เเบบ dataframe ใน pd


        self.n_samples = xy.shape[0]

        self.transform = transform

    def __getitem__(self, index): #อันนี้ได้ใช้ตอนมีอะไรสักอย่างมาเข้าถึง index
        sample =  self.x[index], self.y[index]
        if self.transform:
            sample = self.transform(sample) #ส่ง sample ไปเข้า Class ToTensor เพราะ self.tranfrom = tranform เเละเราได้กำหนด tranform = ToTensor()

        return sample

    def __len__(self):
        return self.n_samples

class ToTensor: 
    def __call__(self, sample): #auto คล้ายๆ init
        inputs, targets = sample
        return torch.from_numpy(inputs), torch.from_numpy(targets) #change numpy to torchTensor and then send back to sample in class Wine

class MulTransform: #การคูณdata ด้วยค่าคงที่ เป็นการปรับเเต่งข้อมูลให้อยู่ในขอบเขตที่เหมาะสม
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, sample):
        inputs, targets = sample
        inputs *= self.factor
        return inputs, targets

dataset = WineDataset(transform=None)
first_data = dataset[0]
features, labels = first_data
print(type(features), type(labels))

composed = torchvision.transforms.Compose([ToTensor(), MulTransform(2)]) #transform เเละ multi ตามลำดับ
dataset = WineDataset(transform=composed)
first_data = dataset[0]
features, labels = first_data
print(type(features), type(labels))
