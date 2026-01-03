%%writefile image_utils.py
import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def load_image(path):
    # Open the image using PIL
    img = Image.open(path)
    # Convert the PIL image object into a NumPy array
    img_array = np.array(img)
    return img_array  # <--- CRITICAL: This must be here

def edge_detection(image_array):
    # 1. Convert to grayscale by averaging
    grayscale = np.mean(image_array, axis=2)

    # 2. Define kernels
    kernelY = np.array([[ 1,  2,  1],
                        [ 0,  0,  0],
                        [-1, -2, -1]])

    kernelX = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    # 3. Apply convolution
    edgeX = convolve2d(grayscale, kernelX, mode='same', boundary='fill', fillvalue=0)
    edgeY = convolve2d(grayscale, kernelY, mode='same', boundary='fill', fillvalue=0)

    # 4. Compute magnitude
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)

    return edgeMAG # <--- CRITICAL: This must be here
