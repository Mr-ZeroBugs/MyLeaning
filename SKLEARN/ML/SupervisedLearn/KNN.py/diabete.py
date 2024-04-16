from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

#read data
df = pd.read_csv("../csvFolder/diabetes.csv")
#data
x = df.drop("Outcome", axis=1).values
# outcome data (answer)
y = df["Outcome"].values

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.4, random_state=0)

#find best neighbor(n) 
k_n = np.arange(1, 9)
trainScore = np.empty(len(k_n))
testScore  = np.empty(len(k_n)) 

for i, k in enumerate(k_n): #loop 1-8
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(xTrain, yTrain)
    trainScore[i] = knn.score(xTrain, yTrain)
    testScore[i] = knn.score(xTest, yTest)

plt.title("compare k values ")
plt.plot(k_n, testScore, label="Testscore") #เอาอันนี้ ที่ score มากสุด มาใช้
plt.plot(k_n, trainScore, label="trainScore") #เอามาดูเทียบเฉยๆ
plt.xlabel("K numb")
plt.ylabel("score")
plt.legend()
#plt.show()

#สรุปใน project นี้ n_nei = 7 ดีสุด
knn2 = KNeighborsClassifier(n_neighbors=8)
knn2.fit(xTrain, yTrain)

predict = knn2.predict(xTest)
print("accurate = ",accuracy_score(yTest, predict)*100,"%")
print(confusion_matrix(yTest, predict))