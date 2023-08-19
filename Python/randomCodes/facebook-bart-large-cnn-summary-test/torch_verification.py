import torch
x = torch.rand(5, 3)
print(x)

print(torch.cuda.is_available()) # should be True

t = torch.rand(10, 10).cuda()
print(t.device) # should be CUDA
