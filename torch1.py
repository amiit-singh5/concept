import torch

a1 = torch.tensor([1.0,2.0,3.0])
print(a1)
b1 = torch.tensor([4.0,5.0,6.0])

print(a1+b1)
print(torch.dot(a1,b1))