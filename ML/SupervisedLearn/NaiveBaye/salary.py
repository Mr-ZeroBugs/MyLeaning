from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("../csvFolder/adult.csv")

#change string to number มันจะจัดกลุ่มให้ โดยเปลี่ยนตัวหนังสือเป็นตัวเลข เเล้วเเบ่งกลุ่ม อิงจากความเหมือนหรือต่างกันของช้อความ เพื่อให้ง่ายต่อการเทรน
def cleandata(dataset):
    for col in dataset.columns: 
        if dataset[col].dtype == type(object):
            le = LabelEncoder()
            dataset[col]=le.fit_transform(dataset[col])
    return dataset

def split_feature_class(dataset, feature):
    answer = dataset["income"].copy()
    datawithoutIncome = dataset.drop(feature, axis=1)
    return datawithoutIncome, answer

df = cleandata(df)
data, answer = split_feature_class(df, "income")
xTrain, xTest, yTrain, yTest = train_test_split(data, answer, random_state=0, test_size=0.2)

#model
model = GaussianNB()

#train
model.fit(xTrain, yTrain)

#predict
predict = model.predict(xTest)

#accuracy
print(accuracy_score(yTest, predict)*100)
