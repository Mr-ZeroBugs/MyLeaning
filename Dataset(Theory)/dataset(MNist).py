#Mnist dataset คือชุดลายมือ เลข 0-9 หลักๆคือให้ai สามารถจำเเนกเลข 0-9 ได้ ในหลายกรณี หลายลายมือ
#training set คือข้อมูลที่เอาไปสอน machine 
#test set ใช้เพื่อทดสอบ model ที่สอนมา โดยทั่วไปจะเเบ่ง training 75%, test25%
from scipy.io import loadmat
import matplotlib.pyplot as plt
mnist_raw = loadmat("mnist-original.mat") #มี70k รูป 28*28
print(mnist_raw)
#รูปภาพที่ 1-60,000 ใช้ trainning 
#รูปที่ 60,001 - 70,000 ใช้ test
mnist = {
    "data" : mnist_raw["data"].T,
    "target" : mnist_raw["label"][0]
}
print(mnist["data"]) #ข้อมูล  pixel ของรูปภาพทั้งหมด
x,y =  mnist["data"], mnist["target"]

number = x[5999] #เเสดงภาพที่ 15,000 ออกมาเป็น pixel
numberImage = number.reshape(28,28)

plt.imshow(numberImage, cmap=plt.cm.binary, interpolation="nearest")
plt.show()
print(y[10000]) #เเสดงออกมาว่าภาพที่ 15,000 คือตัวเลขอะไร(เหมือนเฉลย)