import cv2
import numpy as np
from skeleton_furniture.skeletonizer import Skeletonizer
import pytest

@pytest.fixture
def image():
    # Load a test image
    return cv2.imread('test_image.jpg')

def test_skeletonize(image):
    # Test the skeletonize method
    skeletonizer = Skeletonizer(image)
    skeleton = skeletonizer.skeletonize()
    assert skeleton.shape == image.shape

def test_edge_detection(image):
    # Test the edge detection method
    edge_detector = EdgeDetector(image)
    edges = edge_detector.detect_edges()
    assert edges.shape == image.shape