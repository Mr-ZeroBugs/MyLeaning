import torch
import torch.nn as nn
from sklearn import datasets
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

bc = datasets.load_breast_cancer()
x, y = bc.data, bc.target

n_samples, n_features = x.shape

xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=0, test_size=0.2)
#scale
sc = StandardScaler()
xTrain = sc.fit_transform(xTrain)
xTest = sc.transform(xTest)

xTrain = torch.from_numpy(xTrain.astype(np.float32))
xTest = torch.from_numpy(xTest.astype(np.float32))
yTrain = torch.from_numpy(yTrain.astype(np.float32))
yTest = torch.from_numpy(yTest.astype(np.float32))

yTrain = yTrain.view(yTrain.shape[0], 1) #reshape
yTest = yTest.view(yTest.shape[0], 1)

class LogisticRegression(nn.Module):
    def __init__(self, n_input_features):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(n_input_features, 1)
    
    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x)) #sigmoid จะเเบ่งกลุ่ม ถ้าน้อยกว่า0.5 จะอยู่กลุ่ม0 ถ้ามากกว่า0.5จะอยู่กลุ่ม1
        return y_pred
    
model = LogisticRegression(n_features)

criterion = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

num_epoch = 100
for epoch in range(num_epoch):
    y_pred = model(xTrain)
    loss = criterion(y_pred, yTrain)

    loss.backward()
    optimizer.step()

    optimizer.zero_grad()

    if (epoch+1) % 10 == 0:
        print(f"epoch : {epoch+1}, loss = {loss.item():.4f}")

with torch.no_grad():   
    y_pred = model(xTest)
    y_pred_class = y_pred.round()
    acc = accuracy_score(yTest, y_pred_class)
    print(f"accuracy = {acc:.4f}")

#งานนี้ classification นะ
# acc = y_pred_class.eq(yTest).sum() / float(yTest.shape[0])
#อีกตัวเลือกนึง หากไม่ใช้ accuracy score
#.eq จะไล่เทียบทุกค่าที่ตำเเหน่งเดียวกัน เเล้วคืนค่า t,f จากนัน้ .sum() จะนับ true = 1 เเล้วรวมทั้งหมด เเล้วนำไปหาร rows ทั้งหมด ตัวอย่างเช่น ถูก106ตัว จาก114 ก็106/114 then = 0.92
print(y_pred_class.shape)
print(y_pred_class.eq(yTest).sum())
