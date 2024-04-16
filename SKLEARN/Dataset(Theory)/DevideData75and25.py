from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
print(iris_dataset.data.shape, "is not split")   # row150 column4
x_train,x_test, y_train,y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0, test_size=0.2)
#default คือ 75/25 but อันนี้กำหนด test = 0.2 (20%) เลยกลายเป็น 80/20
#x = data (row150)
#y = target (column4 ชื่อสายพัน)
print(x_train.shape) 
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)