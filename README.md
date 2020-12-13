# 2020-Image-Stylization # 
## Product Description
Photo style transfer is an optimization technique used to modify the style of an image while still preserving its content. It usually takes two images: a content image and a style image. Style transfer will blend two pictures together so the output image looks like the content image, but have the style of the style image.
This is implemented by optimizing the output image to match the content statistics of the content image and the style statistics of the style image, which are extracted from the images using convolutional networks.
The style transfer technique we are using is called WCT.<br>

## Video Demonstration
[![](http://img.youtube.com/vi/RUvS-EWYrbw/0.jpg)](http://www.youtube.com/watch?v=RUvS-EWYrbw "wct")

## File Descriptions

### environment
- environment.yml - Specification for the environment setup.
- env_checker_script.py - Environment checker for the update setup

### data_checker
- checker.py - Checks if the data folder contains the same images as expected.
- download_data.py - Download the images into the data folder.
- save.p - Contains the information about the expected data folder. This is generated by store.py
- store.py - stores the current directory structure of the data folder.


### data_processor
- Dataset.py - A custom dataset class.
- Dataset_train.py - An improved version of the Dataset.py for training purposes. 
- loader_test.py - A test script for data loader.
- metadata.ipynb - Notebook for displaying metadata.
- resize_image.py - Resize the input image to a specific dimension.
- visusalization.ipynb - Notebook for visualizing the images in the data folder

### model_builder
- encoder_decoder.py - The autoencoder model for loading pretrained weights.
- models.py - The autoencoder model with same structure as encoder_decoder but doesn’t load in pretrained weights.
- wct.py - The WCT function for style transfer.
- wct_test.py - Test the WCT function inside the wct.py

### train
- test_train_model.py - Trains the autoencoder model for 40 epochs and saves it

### test
- Photorealistic_Style_Transfer_with_WCT.ipynb - The notebook that contains the result of testing wct using pretrained weights. Performs single layer wct. Test results are in the “the style transfer result demonstration” section. Pretrained weights are here https://drive.google.com/file/d/1M5KBPfqrIUZqrBZf78CIxLrMUT4lD4t9/view 


## Steps to Train
* Install the dependencies
* Run data downloader script in data checker folder or make a directory named “data” and fill it with your image
* Run test_train_model.py

## Notebook link for visualization
https://colab.research.google.com/drive/1Z-7rEHGZTU4XzwwMhDJbMETEBc9vQZuQ?usp=sharing#scrollTo=GRgEODI51CWE <br>
(The demonstration is in the “The Style Transfer Result Demonstration” section and expand it)

## Citations and References
[1] Foamliu, “foamliu/Autoencoder,” GitHub. [Online]. Available: https://github.com/foamliu/Autoencoder. [Accessed: 08-Dec-2020]. <br>
[2] Pietrocarbo, “pietrocarbo/deep-transfer,” GitHub. [Online]. Available: https://github.com/pietrocarbo/deep-transfer. [Accessed: 08-Dec-2020]. <br>
[3] Sunshineatnoon, “sunshineatnoon/PytorchWCT,” GitHub. [Online]. Available: https://github.com/sunshineatnoon/PytorchWCT. [Accessed: 08-Dec-2020]. <br>
[4] Y. Li, C. Fang, J. Yang, Z. Wang, X. Lu, M. Yang, Universal Style Transfer via Feature Transforms, May 2017. [Online] Available: https://arxiv.org/abs/1705.08086v2.
 
 
 