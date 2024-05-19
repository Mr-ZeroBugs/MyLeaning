import torch
import torch.nn as nn
import torch.optim.lr_scheduler as lr_scheduler

lr = 0.1
model = nn.Linear(10, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=lr)
lambda1 = lambda epoch: epoch/10 #meaning lr = epoch / 10 * learning_rate (initial_lr)
scheduler = lr_scheduler.LambdaLR(optimizer, lambda1)

print(optimizer.state_dict())
for epoch in range(5):
    optimizer.step()
    scheduler.step()
    print(optimizer.state_dict()['param_groups'][0]['lr'])
#the reason why the lr of first epoch goes to 0.01 is because model's initial_lr defined by 0.1, so 0.1 * epoch(1)/10 = 0.01
