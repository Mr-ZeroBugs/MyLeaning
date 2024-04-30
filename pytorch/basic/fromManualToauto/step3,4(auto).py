import torch
import torch.nn as nn

x = torch.tensor([[1], [2], [3], [4], [5], [6]], dtype=torch.float32) #data for train
y = torch.tensor([[2], [4], [6], [8], [10], [12]], dtype=torch.float32) #data for train

xTest = torch.tensor([5], dtype=torch.float32)
yTest = xTest*2

n_samples, n_features = x.shape
input_size = n_features
output_size = n_features

#model

class LinearRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegression, self).__init__()
        self.lin = nn.Linear(input_dim, output_dim)
    
    def forward(self, x): #auto sent answer back เพราะ forward มีอยู่เเล้วใน classเเม่ nn.Module
        return self.lin(x)
    
#model = LinearRegression(input_size, output_size) this or
model = nn.Linear(input_size, output_size) #this (is use this, class Linear is trash)


print(f"pred before training : f5 = {model(xTest).item():.3f}") #นี่คือจำนวน x ที่ต้องการ (for examp x = 5 then y must be 10 (Linear Regression))

#train
leaningRate = 0.01
n_iter = 100 #จำนวนรอบ

#loss calculate (auto)
loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=leaningRate)


for epoch in range(n_iter):
    y_pred = model(x)

    l = loss(y, y_pred)

    l.backward()

    #update weight
    optimizer.step()

    optimizer.zero_grad()

    if epoch % 10 == 0:
        [w, b] = model.parameters(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               )
        print(f"epoch {epoch+1}: w = {w[0][0].item():.3f}, loss = {l:.3f}")

print(f"prediction  after training : f(5) = {model(xTest).item():.0f}")
print(f"Actaully answer = {yTest.item()}")