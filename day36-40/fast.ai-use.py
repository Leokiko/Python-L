# # Import fastai library
# from fastai.vision.all import *

# # Load a sample dataset of cats and dogs
# # path = untar_data(URLs.PETS)
# path = r"C:\Users\Rabbit Leo\.cache\torch\hub\checkpoints\resnet34-b627a593.pth"
# # files = get_image_files(path / "images")
# files = get_image_files(path)


# # Define a function to label the images
# def label_func(f):
#     return f[0].isupper()


# # Create a data loader
# dls = ImageDataLoaders.from_name_func(path, files, label_func, item_tfms=Resize(224))

# # Create a convolutional neural network model
# learn = cnn_learner(dls, resnet34, metrics=error_rate)

# # Train the model for 5 epochs
# learn.fine_tune(5)

# Import fastai library
from fastai.vision.all import *
from pathlib import Path

# Load a sample dataset of cats and dogs
path = Path(r"C:\Users\Rabbit Leo\.cache\torch\hub\checkpoints\resnet34-b627a593.pth")
print(path)
files = get_image_files(path)
print(files)


# Define a function to label the images
def label_func(f):
    return f[0].isupper()


# Create a data loader
dls = ImageDataLoaders.from_name_func(path, files, label_func, item_tfms=Resize(224))

# Create a convolutional neural network model
learn = cnn_learner(dls, resnet34, metrics=error_rate)

# Train the model for 5 epochs
learn.fine_tune(epochs=5, verbose=true)
