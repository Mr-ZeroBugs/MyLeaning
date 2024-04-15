from scipy.io import loadmat
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import  cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#yes or no model
mnist_raw = loadmat("mnist-original.mat")
mnist = {
    "data" : mnist_raw["data"].T,
    "target" : mnist_raw["label"][0]
    
}

def displayImage(x):
    plt.imshow(x.reshape(28, 28), cmap=plt.cm.binary, interpolation="nearest")
    plt.show()

def displayPred(clf, actually, xtest):
    print("Is this zero?(Me) = ", actually, "มันคือเลข ", int(yTest[predictNum]))
    print("Is this zero? (Ai) = ",clf.predict([xtest])[0], "มันคือเลข ",int(yTest[predictNum])) #ไม่มีอะไรหรอก เพราะถ้าไม่ใส่0 มันจะเเสดงออกมาโดยมี List


x, y = mnist["data"], mnist["target"]
xTrain, xTest, yTrain, yTest = x[:60000], x[60000:], y[:60000], y[60000:] #เเบ่งเอง จากการ slice


predictNum = 5
yTrain_0 =  yTrain == 0 #เอา yTrain ที่มีค่าเป็น0 เก็บลง yTrain_0
yTest0 = yTest == 0

sgd_clf = SGDClassifier()
sgd_clf.fit(xTrain, yTrain_0)

displayPred(sgd_clf, yTest0[predictNum], xTest[predictNum])

#วัดประสิทธิภาพด้วย Cross validation Test สำหรับเเบ่งข้อมูลออกเป็นหลายๆส่วน
score = cross_val_score(sgd_clf, xTrain, yTrain_0, cv=3, scoring="accuracy")
print(score) #เเบ่งการทดลองวัดเป็น3ครั้ง เเล้วดูว่าเเต่ละรอบเป็นไงบ้าง

#ทำนายผลการทดลอง
y_train_pred = cross_val_predict(sgd_clf, xTrain, yTrain_0, cv=3)
cm=confusion_matrix(yTrain_0, y_train_pred)
print(cm) #เอาง่ายๆนะ ช่อง1 กับ 4 คือ ที่ predict ถูก ส่วน 2กับ3 คือ predict ผิด 

y_test_pred = sgd_clf.predict(xTest)
classnum = ["other num", "num 5"]
print(classification_report(yTest0, y_test_pred, target_names=classnum)) #บอก หลายๆอย่าง ที่จริงๆเเล้วดูเเค่ accurate ก็จบเเล้ว
print("Accurate score = ", accuracy_score(yTest0, y_test_pred)*100, "%") #เเค่นี้ก็พอละ เอาเเค่ accurate


