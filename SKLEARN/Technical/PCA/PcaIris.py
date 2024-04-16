from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import seaborn as sb

iris = sb.load_dataset('iris') #same as iris in sklearn
x, y = iris.drop('species', axis=1), iris['species']

pca = PCA(n_components=3) 
x_pca = pca.fit_transform(x) #เเม่งเอา index ออกให้ด้วย

# add columns
x['pca1'] = x_pca[:, 0] #means all row, column0
x['pca2'] = x_pca[:, 1]
x['pca3'] = x_pca[:, 2]

#ความต่างก็คือมันเป็นการโยนเข้าไปโดยที่ไม่ใช่ข้อมูลดิบ เเต่มีการ add pca เข้าไป 3 columns
xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=0)

xTrain = xTrain.loc[:, ["pca1", "pca2", "pca3"]]
xTest = xTest.loc[:, ["pca1", "pca2", "pca3"]]

model = GaussianNB()
model.fit(xTrain, yTrain)
pred = model.predict(xTest)
print(accuracy_score(yTest, pred)*100)
#ผลลัพะ์เหมือนเดิม เเต่ใช้เวลาน้อยลง
print(xTest)