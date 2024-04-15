import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#การจำลองข้อมูล
rng = np.random
x = rng.rand(50)*10
b = rng.randn(50)
y = 2*x+b

#change data to 2d เพื่อใส่ในโมเดล เพราะมันต้องใช้2มิติ
x2d = x.reshape(-1, 1)

#Linear regressin model
model = LinearRegression()

#train
model.fit(x2d, y)
print(model.score(x2d, y)) #บอกค่าความเเม่นยำ 0-1 ก็เหมือนบอก % ความเเม่นยำอะ เช่นได้0.97 ก็คือึวามเเม่นยำ ประมาณ97%
print(model.intercept_)
print(model.coef_)

#test model
xfit = np.linspace(-1, 11)
xfit2d = xfit.reshape(-1, 1)

yfit =  model.predict(xfit2d)

# analysis model & result
plt.plot(xfit, yfit)
plt.title("Ai predict")
plt.show()
