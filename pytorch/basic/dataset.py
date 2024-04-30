import numpy as np
import torch
import math
from torch.utils.data import Dataset, DataLoader

class WineDataset(Dataset):

    def __init__(self):
        xy = np.loadtxt('wine.csv',delimiter=',', dtype=np.float32, skiprows=1) #skip line1 cuz it's header
        self.x = torch.from_numpy(xy[:, 1:]) #ที่ต้องใส่ torch.fromnumpy เพื่อให้ torch มันสร้าง tensor ให้อะนะ
        self.y = torch.from_numpy(xy[:, [0]])
        self.n_samples = xy.shape[0]
        #เพราะเลือกใช้ numpy.read มันไม่ได้มีfunc เเบบ dataframe ใน pd

    def __getitem__(self, index): #อันนี้ได้ใช้ตอนมีอะไรสักอย่างมาเข้าถึง index
        return self.x[index], self.y[index]

    def __len__(self):
        return self.n_samples

dataset = WineDataset()
dataloader = DataLoader(dataset, batch_size=4, shuffle=True) #num_workers หากจะใช้ ควรมี gpu

#training ;oop
num_epoch = 2
total_sample = len(dataset) #จะไปใช้ def len ใน class WineDataset เเล้ว return n_samples
n_iter = math.ceil(total_sample/4) #it's 4 because of batch (หา index ใหม่)

for epoch in range(num_epoch):
    for i, (input, labels) in enumerate(dataloader):
        if (i+1) % 5 == 0 :
            print(f"epoch = {epoch+1}/{num_epoch}, step {i+1}/{n_iter}, inputs = {input.shape}")
#step 45 มาจาก rows ทั้งหมด 178 /4 (จำนวนbatch) ได้44.5 เเล้วจึงปัดขึ้น
#(การใช้ batch ทำให้ index ลดโดย index/batch size) #enumerate สร้างindexให้   
#input, labels ก็เป็น x, y ใน class WineDataset
#ถามว่าloopเเบบนี้เพื่ออะไร ขอบอกเลยว่ามันเกี่ยวกับกระบวนการเบื้องหลังน่ะ