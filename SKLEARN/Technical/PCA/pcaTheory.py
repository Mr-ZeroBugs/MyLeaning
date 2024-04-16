#ใช้เมื่อมีหลายตัวเเปร จะหา pattern ของเเต่ตัวเเปรเหล่านั้น เเละตัดอันที่ไม่สำคัญทิ้ง ไม่ส่งผลต่อdata
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#n_samble = row, n_feature = columns
x, y = make_blobs(n_samples=100, n_features=10) #ข้อมูลตัวอย่าง
#สร้าง 100rows 10columns เเบบจำนวนมั่วๆ
print("before = ", x.shape)

pca = PCA(n_components=4) #ได้ตั้งเเต่ 1 ถึง จำนวน feature ที่กำหนด  
x = pca.fit_transform(x) #มันจะลด n_feature มันเหลือตามที่กำหนดไว้ใน PCA components
print("after = ",x.shape)

print(pca.explained_variance_ratio_)
plt.bar(["pca1", "pca2", "pca3", "pca4"], pca.explained_variance_ratio_)
#plt.show()