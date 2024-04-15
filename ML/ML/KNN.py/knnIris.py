from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#separate group model

iris_dataset = load_iris()
xTrain, xTest, yTrain, yTest = train_test_split(iris_dataset['data'], iris_dataset['target'],test_size=0.4, random_state=0)

#MOdel
knn = KNeighborsClassifier() #default = 5 (มีนคือถามว่าให้อิงจากจุดใกล้เคียง กี่จุด)

#train
knn.fit(xTrain, yTrain)

#prediction
pred = knn.predict(xTest)
print(pred, "'s the prediction")
print("predict that's in ",iris_dataset['target_names'][pred], "group")
print("-"*10)
print(yTest, "'s the answer")
print(iris_dataset['target_names'][yTest])

print("accuracy = ", accuracy_score(yTest, pred)*100,"%")
