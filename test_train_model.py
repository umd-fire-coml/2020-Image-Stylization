from Dataset_train import CustomTrainDataset
import os
import torch
from skimage import io, transform
import numpy as np
from torch import nn
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
from models import Autoencoder
from torchvision import transforms, utils
import torch.nn.functional as F
learning_rate = 0.0005

model = Autoencoder()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
my_dataset = CustomTrainDataset(path='data')
dataloader = DataLoader(my_dataset, batch_size=4,
                        shuffle=True)

for epoch in range(40):
    for batch_idx, batch in enumerate(dataloader):
        
        # don't need labels, only the images (features)
        image = batch[0]
        out = model(image)
        model.encoder(image)
        cost = criterion(out, image)
        optimizer.zero_grad()
        cost.backward()
        
        ### UPDATE MODEL PARAMETERS
        optimizer.step()
        
        ### LOGGING
    print ('Epoch: %03d/%03d | Batch %03d/%03d | Cost: %.4f' 
                %(epoch+1, epoch, batch_idx, 
                    len(dataloader), cost))
