from keras.models import Model, load_model
from matplotlib import image
from pathlib import Path
import numpy as np

class KerasLoader():

    def __init__(self, model_number: int, base_path: str):
        self.model_number = model_number
        self.base_path = Path(base_path)
        self.model = self.load_net()

    def load_net(self) -> Model:
        model_path = self.base_path / f"Model{self.model_number}.h5"
        return load_model(model_path)

    def predict(self, video_name: str) -> float:
        full_filename = (self.base_path / "Data" / video_name).with_suffix(".jpg")
        example = image.imread(full_filename)
        example = np.expand_dims(example, axis=0)
        result = self.model.predict(example)
        return result[0][0]
