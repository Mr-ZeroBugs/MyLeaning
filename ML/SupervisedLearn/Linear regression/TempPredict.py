import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

TempData = pd.read_csv("https://raw.githubusercontent.com/kongruksiamza/MachineLearning/master/Linear%20Regression/Weather.csv")
x = TempData["MinTemp"].values.reshape(-1, 1)
y = TempData["MaxTemp"].values.reshape(-1, 1)

#80, 20
xTrain, xTest, yTrain, Ytest = train_test_split(x, y, random_state=0, test_size=0.2)

#train
model = LinearRegression()
model.fit(xTrain, yTrain)

#test
yPredict = model.predict(xTest)
#plt.scatter(xTest, Ytest)
#plt.plot(xTest, yPredict, color='r', linewidth=2)
#plt.title("Ai predict")
#plt.show()

# compare true data & predict data
df = pd.DataFrame({"Actually" : Ytest.flatten(), "Predict" : yPredict.flatten()}) #flatten คือเปลี่ยน 2d > 1d
df1 = df.head(20)

df1.plot(kind="bar", figsize=(16, 10))
#plt.show()

#ดูประสิทธิภาพ model, ยิ่งใกล้0 ยิ่งดี
print("MAE = ", metrics.mean_absolute_error(Ytest, yPredict))
print("MSE = ", metrics.mean_squared_error(Ytest, yPredict))
print("RMSE = ", np.sqrt(metrics.mean_squared_error(Ytest, yPredict)))
print("score = ", metrics.r2_score(Ytest, yPredict)) #% accurate (76%)