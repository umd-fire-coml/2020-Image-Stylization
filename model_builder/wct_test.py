from Dataset import CustomDataset
import os
import torch
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
from wct import wct

my_dataset = CustomDataset(path='../data')
dataloader = DataLoader(my_dataset, batch_size=2,
                        shuffle=True)
for i_batch, batch in enumerate(dataloader):
    #all of the batch[i] corresponds to what got returned from the loader    
    #batch[0] is all of the np arrays
    print("batch " + str(i_batch))
    tensors = batch[0]
    f1 = tensors[0]
    f2 = tensors[1]
    res = wct(0.2, f1, f2)[0].numpy()
    plt.imshow(res.astype('uint8'))
plt.show()
