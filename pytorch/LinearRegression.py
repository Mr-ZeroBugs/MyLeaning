from sklearn import datasets
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

#prepare data
X_numpy, Y_numpy = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=1)
x = torch.from_numpy(X_numpy.astype(np.float32))
y = torch.from_numpy(Y_numpy.astype(np.float32))
y = y.view(y.shape[0], 1) #change shape to 1 columns

n_samples, n_features = x.shape


#model
input_size, output_size = n_features, 1
model = nn.Linear(input_size, output_size)

#loss and optimize
learningRate = 0.01
criterion = nn.MSELoss() 
optimizer = torch.optim.SGD(model.parameters(), lr=learningRate)

#training loop
num_epoch = 100 #จำนวนรอบ
for epoch in range(num_epoch):
    y_pred = model(x)
    loss = criterion(y_pred, y)

    #backward
    loss.backward()

    #update
    optimizer.step()
    optimizer.zero_grad()

#plot
predicted = model(x).detach().numpy()
plt.plot(X_numpy, Y_numpy, 'ro')
plt.plot(X_numpy, predicted, 'purple')
#plt.show()

