import cv2
import numpy as np
from skeleton_furniture.contour_detector import ContourDetector
import pytest

@pytest.fixture
def image():
    # Load a test image
    return cv2.imread('test_image.jpg')

def test_contour_detection(image):
    # Test the contour detection method
    contour_detector = ContourDetector(image)
    contours = contour_detector.detect_contours()
    assert len(contours) > 0