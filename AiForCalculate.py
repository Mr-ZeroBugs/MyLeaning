from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import numpy as np

x = np.array([[4, 4], [2, 3], [1, 1], [9, 5], [2, 8], [4, 5], [7, 6], [8, 8], [9, 9], [10, 10]])
y = np.array([8, 5, 2, 14, 10, 9, 13, 16, 18, 20])

xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=0, test_size=0.3)
model = LinearRegression()

#train
model.fit(xTrain, yTrain)
#Test
pred  = model.predict([[10, 205]])
NodotPred = np.round(pred).astype(int)
print(NodotPred[0])