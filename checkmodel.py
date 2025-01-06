import torch
# import torch_ema
# from torch.distributed.checkpoint import load_state_dict
#
# context = 'Pre_train_model/CelebA'
# generator = torch.load('Pre_train_model/CelebA/ema.pth')
generator = torch.load('Output/StyleSDF_Output/checkpoint/Ear422_2/full_pipeline/models_0150000.pt')
# discriminator = torch.load('Output/EarOutputDir4_autodl_64_CARLA/discriminator.pth')
print(generator)
# print(discriminator)

# import torch
# import torch.nn
# import onnx

# model = torch.load('Output/EarOutputDir4_autodl_64_CARLA/generator.pth')
# model.eval()

# input_names = ['input']
# output_names = ['output']
#
# x = torch.randn(1, 3, 32, 32, requires_grad=True)
#
# torch.onnx.export(model, x, 'generator.onnx', input_names=input_names, output_names=output_names, verbose='True')