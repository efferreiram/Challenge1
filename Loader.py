from typing import Union
from torch.nn import Module
from keras.models import Model

class Loader:
    def __init__(self, model_number: int, base_path: str):
        self.model_number = model_number
        self.base_path = base_path
        self.model = self.load_net()

    def load_net(self) -> Union[Model, Module]:
        """Load a Keras or PyTorch model and return it."""
        
        raise NotImplementedError("Function load_net not implemented")
    
    def predict(self, video_name: str) -> float:
        """Revieve a video name as a string and return a prediction as a bool.
        
        The name recieved as a string does not contain the extension. For example,
        if the video name "is 1_3_47_1.avi", this function will only recieve the
        string "1_3_47_1".

        The float returned must be in the range [0, 1], the closer it is to 1, the
        more likely it is to be an attack.
        """

        raise NotImplementedError("Function predict not implemented")