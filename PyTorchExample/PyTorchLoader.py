import cv2 as cv
import numpy as np
import torch
from PIL import Image
from torch import nn
from torch.nn import Module
from torchvision import models
from pathlib import Path


class PyTorchLoader():

    def __init__(self, model_number, base_path):
        self.model_number = model_number
        self.base_path = Path(base_path)
        self.model = self.load_net()


    def load_net(self) -> Module:
        net = PyTorchNN()
        model_path = self.base_path / f"Model{self.model_number}.pth"
        net.load_state_dict(torch.load(str(model_path))["state_dict"])
        net.eval()
        return net

    def predict(self, video_name: str) -> float:
        full_filename = (self.base_path / "Data" / video_name).with_suffix(".jpg")
        img = np.asarray(Image.open(full_filename))
        resized = cv.resize(img, (224, 224), interpolation=cv.INTER_AREA)
        resized = np.moveaxis(resized, -1, 0)
        resized = np.expand_dims(resized, axis=0)
        tensor = torch.Tensor(resized)
        out = self.model.forward(tensor)
        return out[1].item()


class PyTorchNN(Module):

    def __init__(self, pretrained=True):
        super().__init__()
        dense = models.densenet161(pretrained=pretrained)
        features = list(dense.features.children())
        self.enc = nn.Sequential(*features[0:8])
        self.dec = nn.Conv2d(384, 1, kernel_size=1, padding=0)
        self.linear = nn.Linear(14 * 14, 1)

    def forward(self, img):
        enc = self.enc(img)
        dec = self.dec(enc)
        dec = nn.Sigmoid()(dec)
        dec_flat = dec.view(-1, 14 * 14)
        op = self.linear(dec_flat)
        op = nn.Sigmoid()(op)
        return dec, op
