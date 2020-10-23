import cv2
import numpy as np
from PIL import Image
# from matplotlib import image
# from matplotlib import pyplot

# input a numpy array of a image and return the cropped and resized array
def resize_image(img_arr, resize_width = 256, resize_height = 256):
    height, width, dim = img_arr.shape
    
    # Crop the image to square
    if width != height:
        offset  = int(abs(height - width)/2)
        if width > height:
            img_arr = img_arr[:,offset:(width - offset),:]
        else:
            img_arr = img_arr[offset:(height - offset),:,:]
    
    # Resize the image to specific size
    dim = (resize_width, resize_height)
    img_arr = cv2.resize(img_arr, dim, interpolation = cv2.INTER_AREA)
    return img_arr


# def visualization():
#     image = Image.open(r"<ImageNameHere>")
#     image_cropped = crop_image(np.array(image))
#     result = Image.fromarray(image_cropped)
#     pyplot.imshow(result)
#     pyplot.show()