#ดอก Iris สาเหตุที่เริ่มทด้วย Iris คือมีนเป็น base ที่เข้าใจง่าย หลักๆบทนี้คือจะสอนให้AI เเยกประเภทดอกไม้ด้วยการจำเเนกจากข้อมูลบลาๆ
#dataSet คือ การนำข้อมูลที่ลักษณะเหมือนกัน มาจัดเป็นชุดตามลักษณะ
from sklearn import datasets
datasetIris = datasets.load_iris()

print(datasetIris.keys()) #ดูว่ามี key ไรบ้าง
print(datasetIris['target_names']) #ดูชื่อสายพันธุ์ ใช้ " " ไม่ได้ ไม่รู้ทำไม 
print(datasetIris['DESCR']) #บอกข้อมูลเเทบทุกอย่าง ของทั้ง3สายพันธุ์
print(datasetIris['feature_names']) #มันจะบอกว่า ข้อมูลนั้น มันบอกอะไรบ้าง เป็นหัวข้อจากตารางการทดลอง
print(datasetIris['data'][:5]) #เอามา5บรรทัดพอ มันโชว์ข้อมูลตารางการทดลองเป็นตัวเลข 150 บรรทัด ไม่ต้องรันหรอก เเม่งยาว
print(datasetIris['target'])
