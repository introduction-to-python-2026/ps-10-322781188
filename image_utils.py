from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    import numpy as np
from PIL import Image

def load_image(path):
    # Open the image using PIL
    img = Image.open(path)
    
    # Convert the PIL image object into a NumPy array
    img_array = np.array(img)
    
    return img_array

def edge_detection(image):
    import numpy as np
from scipy.signal import convolve2d

def edge_detection(image_array):
    # 1. Convert to grayscale by averaging the three color channels
    # Note: We average across axis 2 (the color channels)
    grayscale = np.mean(image_array, axis=2)

    # 2. Define the kernels (filters)
    kernelY = np.array([[ 1,  2,  1],
                        [ 0,  0,  0],
                        [-1, -2, -1]])

    kernelX = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    # 3. Apply convolution with zero padding ('same' ensures output size matches input)
    edgeX = convolve2d(grayscale, kernelX, mode='same', boundary='fill', fillvalue=0)
    edgeY = convolve2d(grayscale, kernelY, mode='same', boundary='fill', fillvalue=0)

    # 4. Compute the magnitude of the edges
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)

    return edgeMAG
