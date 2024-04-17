#ใช้เพื่อเเบ่งข้อมูลเป็น2ส่วน เหมือนเป็นการตีเส้น เเบบ Linear regression
#btw เเม่งรันโคตรนาน
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix


faces = fetch_lfw_people(min_faces_per_person=60) #60 faces import (not the total of images, it's just total of faces)
print(faces['target_names']) #people names
print(faces['images'].shape) # 1348 images

fig, ax = plt.subplots(3, 5)
for i, axi in enumerate(ax.flat):
    axi.imshow(faces['images'][i])
    axi.set(xticks=[], yticks=[]) #นี่คือการบอกว่าไม่ต้อง show ข้อมูลข้างๆกรอบ พวกความสูงบลาๆ
    axi.set_xlabel(faces.target_names[faces.target[i]].split()[-1], color='black')
#plt.show()

#reduce by svm
pca = PCA(n_components=200, svd_solver="randomized", whiten=True)
svc = SVC(kernel='rbf', class_weight="balanced")

model = make_pipeline(pca, svc) #รวมทั้ง2 เข้าด้วยกัน

#split
xTrain, xTest, yTrain, yTest = train_test_split(faces['data'], faces['target'], random_state=20, test_size=0.2)

#find best value of c and g
bestValue = {"svc__C":[1, 5, 10, 50], "svc__gamma":[0.0001, 0.0005, 0.001, 0.005]} #ตรง svx__C, gamma ต้องเขียนเเบบนี้เท่านั้น
grid = GridSearchCV(model, bestValue)
grid.fit(xTrain, yTrain)
#print(grid.best_params_ )#show Best value
#print(grid.best_estimator_) #show all setting about our model

#ใช้จริง
model = grid.best_estimator_
pred = model.predict(xTest)
print(accuracy_score(yTest, pred))
print(confusion_matrix(yTest, pred))