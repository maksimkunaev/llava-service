import torch

if torch.cuda.is_available():
    print('LLAVA is running on GPU.!!!!!!!!!!!!!!!????????/')
    print("CUDA is available. Current device: ", torch.cuda.current_device())
    print("Device name: ", torch.cuda.get_device_name(
        torch.cuda.current_device()))
else:
    print("CUDA device not available.")
