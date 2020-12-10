from Dataset import CustomDataset
import os
import torch
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
my_dataset = CustomDataset(path='../data')
dataloader = DataLoader(my_dataset, batch_size=8,
                        shuffle=True)

"""
 - Dataset Obj. name
 - command line inputs for batch_size, num_workers, path
 
 batch_size:
 - max out GPU memory by increasing batch_size
 - play with batch_sizes as powers of 2, not TOTALLY necessary
    - if not a power of two, may make training much slower
"""

#testing the dataset
print("dataset test")
#expected is first image dimension and name of the dataset
print(my_dataset[0][0].shape)
print(my_dataset[0][1])
#testing the script
print("dataloader test")
for i_batch, batch in enumerate(dataloader):
    #all of the batch[i] corresponds to what got returned from the loader    
    #batch[0] is all of the np arrays
    print("batch " + str(i_batch))
    for x in batch[0]:
        print(x.shape)
    #batch[1] is all of the names
    for x in batch[1]:
        print(x)