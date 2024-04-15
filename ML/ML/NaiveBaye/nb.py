from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

#เเบ่งกลุ่มเอง โดยอาจมีหลายกลุ่ม
irisd = load_iris()
x,y = irisd['data'], irisd['target'] #ตามทฤษฎี y คือ class(c)

#devide
xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=0)

#model
model = GaussianNB()
#train
model.fit(xTrain, yTrain)

#prediction
predict = model.predict(xTest)

#score
print(accuracy_score(predict, yTest)*100,"%")
print(xTest)