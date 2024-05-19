import torch
import torch.nn as nn
import torch.optim.lr_scheduler as lr_scheduler

lr = 0.1
model = nn.Linear(10, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=lr)
lambda1 = lambda epoch: 0.95 #meaning lr = last lr * 0.95
scheduler = lr_scheduler.MultiplicativeLR(optimizer, lambda1)

print(optimizer.state_dict())
for epoch in range(5):  
    optimizer.step()
    scheduler.step()
    print(optimizer.state_dict()['param_groups'][0]['lr'])

#here's the reason why
#epoch 1: LR เริ่มต้น = 0.1 * 0.95 = 0.095
#epoch 2: LR เก่า = 0.095 * 0.95 = 0.09025
#epoch 3: LR เก่า = 0.09025 * 0.95 = 0.0857375
#epoch 4: LR เก่า = 0.0857375 * 0.95 = 0.08145062499999998
#epoch 5: LR เก่า = 0.08145062499999998 * 0.95 = 0.07737809374999999