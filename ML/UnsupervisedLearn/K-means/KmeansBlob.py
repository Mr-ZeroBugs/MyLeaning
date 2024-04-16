from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#ใช้ accurate score ไม่ได้ละนะ train_spilit ด้วย
#เรื่องนี้ มันไม่ใช่การหาคำตอบเเบบที่เคนเรียนมา มันเป็นการทำนายกลุ่มมากกว่า ว่าdata นั้นๆ ควรอยู่กลุ่มไหน
#sort group auto
x,y = make_blobs(n_samples=300, centers=4, random_state=0, cluster_std=0.5) #ไอ้ตรง center มันคือการถามว่า จะให้ข้อมูลมีกี่กลุ่ม เเล้วข้อมูลที่ random ออกมา จะใกล้เคียงกัน ตามจำนวนกลุ่มที่เขียนไว้
model = KMeans(n_clusters=4) #เลือกว่าจะเเบ่งกี่กลุ่ม สามารถเเบ่งตาม center ด้านบนก็ได้นะ เเต่ข้อมูลจริงคงต้องไปดูอีกทีว่าเเนวโน้มมัน เเบ่งได้กี่กลุ่ม
model.fit(x)
pred = model.predict(x)
centroid = model.cluster_centers_ 

plt.scatter(x[:,0], x[:,1], c=pred) #กำหนดสีเอง ตามจำนวนกลุ่ม
plt.scatter(centroid[0, 0], centroid[0, 1], c='purple', label="cen1", s=100)
plt.scatter(centroid[1, 0], centroid[1, 1], c='yellow', label="cen2", s=100)
plt.scatter(centroid[2, 0], centroid[2, 1], c='red', label="cen3", s=100)
plt.scatter(centroid[3, 0], centroid[3, 1], c='orange', label="cen4", s=100)

#new point for test auto sort
xTest, yTest = make_blobs(n_samples=10, centers=4, cluster_std=0.5, random_state=0)
predXtest = model.predict(xTest) #ให้โมเดลทำนายว่า xTest ควรอยู่สีอะไร

#test
plt.scatter(xTest[:, 0], xTest[:, 1], c=predXtest, s=200) #ปรับขนาดใหญ่ๆเพื่อให้รู้ว่าก้อนนั้นคือ xTest เเละถ้าสีตรงตามกลุ่ม ก็คือpredict ถูกต้อง

plt.legend(frameon=True)
#plt.show()
