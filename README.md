# Introduction

A Flask web application that uses a fine-tuned VGG16 model for predicting dogs and cats. This flask web application determines if an uploaded image is of a cat or a dog using a fine-tuned VGG16 model. The VGG16-fine-tuned model is from this repository's Jupyter notebook and was transformed into a sequential model with predictions for just the two classes of cats and dogs. After that, this sequential model was trained using 1300 images from each class. The Jupyter notebook's "model.h5" file contains a completed and reusable model. Important information about the arrangement of the image directories can be found in the notebook. Lastly, this h5 file is loaded by the Flask web server, which makes use of it to generate predictions.

# Dependencies

The project requires the following:

- python 3.10.x
- numpy 1.24.3
- tensorflow 2.13.0
- keras 2.13.1 
- flask 2.3.2
  
# Datasets

