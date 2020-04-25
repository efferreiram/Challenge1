
# Deep Learning Class Challenge #1 Competition Evaluator
The following file describes what students need to do in order to set up their model for evaluation in the competition.

## The process
This process consists of 2 main steps:
1. Implement your own python class based on the provided example `Loader.py` class.
2. Order your files and code in the way specified below.

### Implement your own python class
For it to be a fair competition, you have to use the file `Loader.py` provided as the base class for your own. You have to implement the methods `load_net` and `predict`, respecting their signatures. In the case of load_net, you can use either a Keras `Model` or PyTorch `Module` and then delete the type hint for the other. For simplicity, just change the Loader file, you do not have to inherit from it.

We provide two examples for this kind of loader, one for Keras and one for PyTorch. In the case of Keras, you can easily save the model whole, including the architecture, by following the steps [here](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model). In the case of PyTorch, only the weights can be easily saved, so we recommend to annex the class containing the architecture of the network in the same file and instantiating it before loading the weights, it is shown on the example, but for more information, check [here](https://pytorch.org/tutorials/beginner/saving_loading_models.html).

We are basically going to do what we show in `Test_classes.py`, So it may give you an idea of how things works.

## Structure of the expected compressed file:
```
TeamName.[zip, rar, tar]
+- Loader.py - File with the code used to load your network and evaluate a single image. See the anexed Loader.py for the base class
+- Models
| +- Model1.h5 | Model1.pth - For Keras and PyTorch respectively
| +- Model2.h5 | Model2.pth - For Keras and PyTorch respectively
| +- Model3.h5 | Model3.pth - For Keras and PyTorch respectively
| +- Model4.h5 | Model4.pth - For Keras and PyTorch respectively
| +- Model5.h5 | Model5.pth - For Keras and PyTorch respectively
| +- Model6.h5 | Model6.pth - For Keras and PyTorch respectively
+- Data - Where the videos or sampled images are
| +- 2_1_21_1.jpg
| +- 2_1_21_2.avi
| +- ...
```

**REMEMBER TO KEEP THE SAME FILENAMES(INCLUDING USE OF CAPS) FOR EASIER EVALUATION**

## Authors
- Emilio Ferreira @efferreiram <A01020938@itesm.mx>
- Jacob Rivera @edjacob25 <A01184125@itesm.mx>

If you have any questions or observations, don't hesitate to open an issue in github so everybody can see it after.