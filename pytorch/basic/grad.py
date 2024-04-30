import torch
x = torch.randn(3, requires_grad=True) #grad มันจะบอกว่าตัวนี้ๆ มาจากไหน ผ่านกระบวนการอะไรมา เช่น add sub (+, -)
y = x-2
print(y)

#calculate the gradient
z = (y*y).mean() #do this first before .backward()
print(z)
z.backward() #before this, you have to send other variable to do something like .mean(), .sum() first for change it to be scalar (scalar คือมีเเค่1 member ใน array)
print(x.grad) #now u can see the gradient of x 

#delete req grad
#print(x.requires_grad_(False)) 
newXwithoutReq = x.detach() #it will create new variable that the same value but without req grad
print(newXwithoutReq)

with torch.no_grad():
    y = x + 2 
    print(y) #all in this func won't have req grad(its public)

