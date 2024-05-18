import torch
import torch.nn as nn

class Model(nn.Module): #Linear Simulation
    def __init__(self, n_input_features):
        super(Model, self).__init__()
        self.linear = nn.Linear(n_input_features, 1) 

    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

model = Model(n_input_features=6)
learning_rate = 0.01
num_epoch = 100
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
print(optimizer.state_dict())
for param in model.parameters():
    print(param)

#Saving model that still not completed training yet
checkpoint = {
    "epoch": 90,
    "model_state" : model.state_dict(),
    "optim_state" : optimizer.state_dict()
}

torch.save(checkpoint, "not_finished_trainning_yet.pth") #no need to delete or change this line to comment
loaded_model = torch.load("not_finished_trainning_yet.pth")

model = Model(n_input_features=6)
optimizer =  torch.optim.SGD(model.parameters(), lr=0) #ไม่จำเป็นตรง lr ต้องกำหนดใหม่ เดี๋ยวมันปรับให้ตามที่เคยกำหนด

epoch = loaded_model["epoch"]
model.load_state_dict(checkpoint["model_state"])
optimizer.load_state_dict(checkpoint["optim_state"])

print(optimizer.state_dict())

#Saving model for testing or ready to use
torch.save(model.state_dict(), "FinishedModel.pth") #you dont have to delete or change this line to comment when you have already loaded
loaded_finishedModel = Model(n_input_features=6)
loaded_finishedModel.load_state_dict(torch.load("FinishedModel.pth"))
loaded_finishedModel.eval()
for param in loaded_finishedModel.parameters():
    print(param)
#initially, the way to check model's accuracy you can print params and if it's the same params as origin model, that means it's the same accuracy as origin model you've already trained