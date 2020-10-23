'''
https://pytorch.org/tutorials/beginner/data_loading_tutorial.html#dataset-class
'''
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import os
import numpy as np
import torch
from os import listdir
from os.path import join
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
from skimage import io, transform
from resize_image import resize_image

#the custom dataset
class CustomDataset(Dataset):
    def __init__(self,path='data'):
        #get all of the files and under the path
        self.files = os.listdir(path)
        self.cur_directory = os.path.join(os.getcwd(), path) 

    #get item returns the item at index which is also used in loader 
    def __getitem__(self,index):        
        image_path = os.path.join(self.cur_directory,self.files[index])
        image = io.imread(image_path)
        #image preprocessing
        #do some preprocessing if needed
        #return
        
        #the order is imageio array, file name
        npa = np.asarray(image)
        npa = resize_image(image)
        #index[0] of what gets returned is the image np array 
        #index[1] is file name
        return npa, self.files[index]

    def __len__(self):
        return len(self.files)

