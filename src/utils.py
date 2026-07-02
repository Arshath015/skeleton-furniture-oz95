import cv2
import numpy as np

def resize_image(image: np.ndarray, size: tuple) -> np.ndarray:
    # Resize the image to the specified size
    return cv2.resize(image, size)

def normalize_image(image: np.ndarray) -> np.ndarray:
    # Normalize the image to have zero mean and unit variance
    return (image - np.mean(image)) / np.std(image)