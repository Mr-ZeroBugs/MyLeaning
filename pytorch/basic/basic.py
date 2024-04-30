import torch
import numpy as np

#เอาง่ายๆนะ มี basic เเบบ numpy เลย
x = torch.empty(1, 2, 3) #1floor 2rows 3columns (3d, (random nums))
x2 = torch.ones(2,2, dtype=torch.double) #float 64 เเต่เเค่ show ใน print ความต่างของ float 16 32 64 คือพื้นที่ เเละ ประสิทธิภาพ
x3 = torch.tensor([[2.5, 0.1], [2.4, 4.5]]) #crate value by your self

x3.add_(x2) #its mean  x3 + x2
x3.sub_(x2) # minus
x3.mul_(x2) # multiple
x3.div_(x2) # divide

print(x3[0][0].item()) #item means change to show only number
#.values() means chnage to show tensor
b = x.numpy() #change to numpy array
c = torch.from_numpy(b) # change numpy to tensor
print(type(b))
print(type(c))

