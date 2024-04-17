from scipy.io import loadmat
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

mnist_raw = loadmat("mnist-original.mat") 
mnist = {
    "data" : mnist_raw["data"].T,
    "target" : mnist_raw["label"][0]
}
x, y =  mnist["data"], mnist["target"]
xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=0, test_size=0.15)

fig, ax = plt.subplots(10, 10, figsize=(8,8), subplot_kw={"xticks":[], "yticks":[]}, gridspec_kw = dict(hspace=0.1, wspace=0.1))
#for i, axi in enumerate(ax.flat):
    #axi.imshow(xTrain[i].reshape(28, 28), cmap='binary', interpolation="nearest")
    #axi.text(0.05, 0.05, str(int(yTrain[i])), transform = axi.transAxes, color="black")
#plt.show()

#model
model = MLPClassifier()
model.fit(xTrain, yTrain)

pred = model.predict(xTest)
print(accuracy_score(yTest, pred))

for i, axi in enumerate(ax.flat):
    axi.imshow(xTest[i].reshape(28, 28), cmap='binary', interpolation="nearest")
    axi.text(0.05, 0.05, str(int(pred[i])), transform = axi.transAxes, color="green" if pred[i] == yTest[i] else "red")
plt.show()
