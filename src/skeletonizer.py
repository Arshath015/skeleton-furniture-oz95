import cv2
import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass
class Skeletonizer:
    image: np.ndarray

    def skeletonize(self) -> np.ndarray:
        # Apply the Medial Axis Transform (MAT) algorithm to skeletonize the image
        kernel = np.ones((3, 3), np.uint8)
        eroded_image = cv2.erode(self.image, kernel, iterations=1)
        dilated_image = cv2.dilate(self.image, kernel, iterations=1)
        skeleton = cv2.bitwise_and(dilated_image, cv2.bitwise_not(eroded_image))
        return skeleton

@dataclass
class EdgeDetector:
    image: np.ndarray

    def detect_edges(self) -> np.ndarray:
        # Apply the Canny edge detection algorithm to detect edges in the image
        blurred_image = cv2.GaussianBlur(self.image, (5, 5), 0)
        edges = cv2.Canny(blurred_image, 50, 150)
        return edges

@dataclass
class ContourDetector:
    image: np.ndarray

    def detect_contours(self) -> np.ndarray:
        # Apply the OpenCV contour detection algorithm to detect contours in the image
        contours, _ = cv2.findContours(self.image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours