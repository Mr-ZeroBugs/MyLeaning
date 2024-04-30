import torch
import numpy as np #all manual

x = torch.tensor([1, 2, 3, 4], dtype=torch.float32) #data for train
y = torch.tensor([2, 4, 6, 8], dtype=torch.float32)

w = torch.tensor(0.0, requires_grad=True, dtype=torch.float32) #in the end, 2

#pred
def forward(x):
    return w*x
#loss calculate
def loss(y, pred):
    return ((pred-y)**2).mean()



print(f"pred before training : f5 = {forward(6):.3f}") #นี่คือจำนวน x ที่ต้องการ

#train
leaningRate = 0.01
n_iter = 100 #จำนวนรอบ

for epoch in range(n_iter):
    y_pred = forward(x)

    l = loss(y, y_pred)

    l.backward()

#update weight
    with torch.no_grad():
        w -=  leaningRate * w.grad

    w.grad.zero_()
    if epoch % 10 == 0:
        print(f"epoch {epoch+1}: w = {w:.3f}, loss = {l:.3f}")

print(f"prediction  after training : f(5) = {forward(6):.3f}")
#loss ลดลงทุกครั้ง
#หา pattern ระหว่าง x เเละ y (Linear regression)