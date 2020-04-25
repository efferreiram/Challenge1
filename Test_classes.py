from KerasExample.KerasLoader import KerasLoader
from PyTorchExample.PyTorchLoader import PyTorchLoader
from pathlib import Path

model_number = 1
base_path = "KerasExample"
mod = KerasLoader(model_number, base_path)
res = mod.predict("1_3_47_1")
print(f"The result from Keras is {res}")

model_number = 1
base_path = "PyTorchExample"
mod2 = PyTorchLoader(model_number, base_path)
res2 = mod2.predict("1_3_47_1")
print(f"The result from PyTorch is {res2}")

