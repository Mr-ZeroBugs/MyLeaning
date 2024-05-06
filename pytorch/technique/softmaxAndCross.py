import torch
import torch.nn as nn
import numpy as np

def Softmax(x):
        return np.exp(x) / np.sum(np.exp(x), axis=0) #exp คือการนำค่าe ไปยกกำลัง items ใน array (e คือค่าคงตัว = 2.71828 เรียก่า exponential)

x = np.array([2.0, 1.0, 0.1])
outputs = Softmax(x)
#print("softmax = ", outputs)
#softmax คือการนำ items ใน array ไปลดค่า โดยจะมีผลรวมได้ 1 โดย items ที่มีผลมากที่สุด ก็จะมีเลขเยอะ
#เช่น 2.0 = 0.65, 1.0 = 0.24,  0.1 : 0.09 ตามค่าของการมีผลของเเต่ละตัว ซึ่งรวมๆกันก็เป็น1

#softmax by attribute in pytorch
x = torch.tensor([2.0, 1.0, 0.1])
outputs = torch.softmax(x, dim=0)
#print(outputs)

#cross
loss = nn.CrossEntropyLoss() #มันรวม softmax ไว้เเล้ว ไม่ต้องไป soft ก่อน, หรือหลัง

# samples = 3 (len(y))
# classes = your define สมมติจะทำModel ที่เเยก เเมว, หมา then classes = 2
y = torch.tensor([2, 0, 1])

# nsamples * nclasses = 3*3     
ypredGood = torch.tensor([[0.1, 1.0, 2.1], [2.0, 1.0, 0.1], [1.0, 3.0, 0.1]]) #[2, 0, 1] good เรียงให้ตัวที่มากที่สุดของเเต่ละ rows อยู่ใน index = y เช่นอันนี้ตัวที่มากที่สุดของเเต่ละrow อยู่indexที่ [2, 0, 1] ซึ่งตรงกับ y
ypredBad = torch.tensor([[2.1, 1.0, 0.1], [0.1, 1.0, 2.1], [1.0, 3.0, 0.1]]) #เรียงมั่ว (bad)[0,2,1]

l1 = loss(ypredGood, y)
l2 = loss(ypredBad, y)
print(l1.item()) #low loss rate
print(l2.item()) #high loss rate because of bad sort

value1, index1 = torch.max(ypredGood, 1) #1dim
value2, index2 = torch.max(ypredBad, 1)
print(index1) #จะสื่อว่า ตัวที่มีค่ามากที่สุด อยู่indexที่0 
print(index2) #จะสื่อว่า ตัวที่มีค่ามากที่สุด อยู่indexที่1

#สรุปคือ these two ส่วนมากจะใช้ปรับข้อมูลในการ trainning ใน deeplearning ประเภท classification
#(หากจะใช้ cross อย่าใช้ softmax เพราะ cross มี softmax ในตัวเองอยู่เเล้ว
