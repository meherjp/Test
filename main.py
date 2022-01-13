import torch
device= "cuda" if torch.cuda.is_available() else "cpu"
my_tensor=torch.tensor([[1,2,3], [4,5,6]])
print(my_tensor)
print(torch.empty(size=(3,3)))
print(torch.rand(3,4))
print(torch.eye(3,4))
print(torch.__version__)