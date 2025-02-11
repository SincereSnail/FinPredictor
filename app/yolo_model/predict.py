import numpy as np
import torch

def predict_stock_price(ticker : str) :
    model = torch.load("yolo_stock_model.pth")
    input_data = np.random.rand(1,10,10)
    input_tensor = torch.tensor(input_data).float().unsqueeze(0)
    output = model(input_tensor)
    return output.item()