from scipy.io import loadmat
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

mnist_raw = loadmat("mnist-original.mat")
mnist = {
    "data" : mnist_raw["data"].T,
    "target" : mnist_raw["label"][0]
}
xTrain, xTest, yTrain, yTest = train_test_split(mnist["data"], mnist["target"], random_state=0)

pca = PCA(0.95) #ลดขนาดรูปจาก 784 > 154
xTrain = pca.fit_transform(xTrain) 
result = pca.inverse_transform(xTrain) #เปลี่ยนกลับเพื่อทำให้มันเเสดงใน matplot ได้เฉยๆ ไม่ได้เอาไปใช้เทรน
# อย่าลืม xTest ด้วยใช้เเค่tranform ไม่ต้องfit เเต่พวกy ไม่ต้องใช้เลย (สำหรับเทรน) 
xTest = pca.transform(xTest)


#show image 784
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.title("original")
plt.xlabel("784, origin")
plt.imshow(mnist["data"][0].reshape(28,28), cmap=plt.cm.gray, interpolation="nearest")

# 154
plt.subplot(1,2,2)
plt.imshow(result[0].reshape(28,28), cmap=plt.cm.gray, interpolation="nearest")
plt.xlabel(["154, PCA"])
plt.title("PCA")
#plt.show() #หากเป็นภาพเดียวกัน คือทำถูก

model = KNeighborsClassifier()

model.fit(xTrain, yTrain)
pred = model.predict(xTest)
print(accuracy_score(yTest, pred)*100)

