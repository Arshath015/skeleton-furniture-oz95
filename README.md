# Image Skeletonization for Furniture CAD

[![Python Version](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/release/python-390/) [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Build Status](https://img.shields.io/badge/Build-Passing-green.svg)](https://github.com/user/skeleton-furniture/actions) [![Code Style](https://img.shields.io/badge/Code%20Style-Black-black.svg)](https://github.com/psf/black)

This submodule is part of the AIERA CAD project, an AI-powered architectural assistant that transforms furniture photos into precise 2D CAD-style technical drawings and orthographic blueprints.

## Table of Contents
* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Theoretical Background](#theoretical-background)
* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Case Studies](#case-studies)
* [Testing](#testing)
* [Performance Considerations or Limitations](#performance-considerations-or-limitations)
* [Roadmap](#roadmap)
* [License](#license)

## Overview
The goal of this submodule is to provide a robust and efficient way to transform furniture photos into precise 2D CAD-style technical drawings and orthographic blueprints using image skeletonization. This technique is particularly useful for furniture design, as it allows for the creation of clean and minimal line drawings that can be easily edited and modified.

## Tech Stack
* Python 3.9
* OpenCV 4.5
* NumPy 1.20
* Pillow 8.2
* Pydantic 1.8
* Dataclasses 0.6

## Architecture
```mermaid
graph LR
    A[Furniture Photo] -->|Image Preprocessing|> B[Image Skeletonization]
    B -->|Edge Detection|> C[Contour Detection]
    C -->|Threshold and Binarization|> D[Line Simplification and Vectorization]
    D -->|DXF/SVG Export|> E[2D CAD-Style Technical Drawings and Orthographic Blueprints]
```
The architecture of this submodule consists of the following components:
* Image Preprocessing: This step involves resizing and normalizing the input image.
* Image Skeletonization: This step uses the Medial Axis Transform (MAT) algorithm to skeletonize the input image.
* Edge Detection: This step uses the Canny edge detection algorithm to detect edges in the skeletonized image.
* Contour Detection: This step uses the OpenCV contour detection algorithm to detect contours in the edge-detected image.
* Threshold and Binarization: This step applies threshold and binarization analysis to the contour-detected image to generate a clean and minimal line drawing.
* Line Simplification and Vectorization: This step simplifies and vectorizes the line drawing using the Ramer-Douglas-Peucker algorithm.
* DXF/SVG Export: This step exports the simplified and vectorized line drawing in DXF and SVG formats.

## Theoretical Background
Image skeletonization is a technique used to reduce a binary image to its skeleton, which is a set of pixels that represent the medial axis of the image. The Medial Axis Transform (MAT) algorithm is a popular method for skeletonizing images, which works by iteratively eroding the image until only the medial axis remains. The MAT algorithm has several advantages over other skeletonization algorithms, including its ability to preserve the topology of the image and its robustness to noise.

The Canny edge detection algorithm is a widely used method for detecting edges in images. It works by applying a Gaussian filter to the image to reduce noise, followed by a non-maximum suppression step to thin the edges. The Canny algorithm has several parameters that need to be tuned, including the threshold values and the aperture size of the Sobel operator.

The OpenCV contour detection algorithm is a method for detecting contours in images. It works by finding the boundaries of objects in the image and representing them as a sequence of points. The contour detection algorithm has several parameters that need to be tuned, including the threshold value and the minimum area of the contour.

## Installation
To install this submodule, run the following command:
```bash
pip install -r requirements.txt
```

## Usage
To use this submodule, import the `Skeletonizer` class and call the `skeletonize` method:
```python
from skeleton_furniture.skeletonizer import Skeletonizer

# Load the input image
image = cv2.imread('input_image.jpg')

# Create a Skeletonizer object
skeletonizer = Skeletonizer(image)

# Skeletonize the image
skeleton = skeletonizer.skeletonize()

# Display the skeleton
cv2.imshow('Skeleton', skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## API Reference
* `Skeletonizer` class:
    + `__init__`: Initializes the Skeletonizer object with the input image.
    + `skeletonize`: Skeletonizes the input image using the Medial Axis Transform (MAT) algorithm.
* `EdgeDetector` class:
    + `__init__`: Initializes the EdgeDetector object with the input image.
    + `detect_edges`: Detects edges in the input image using the Canny edge detection algorithm.
* `ContourDetector` class:
    + `__init__`: Initializes the ContourDetector object with the input image.
    + `detect_contours`: Detects contours in the input image using the OpenCV contour detection algorithm.

## Case Studies
* Case Study 1: Furniture Design
    + Input: A photo of a chair
    + Output: A clean and minimal line drawing of the chair
    + Description: The submodule is used to transform a photo of a chair into a precise 2D CAD-style technical drawing and orthographic blueprint.
* Case Study 2: Architectural Design
    + Input: A photo of a building
    + Output: A clean and minimal line drawing of the building
    + Description: The submodule is used to transform a photo of a building into a precise 2D CAD-style technical drawing and orthographic blueprint.

## Testing
To run the test suite, execute the following command:
```bash
pytest tests/
```

## Performance Considerations or Limitations
The performance of this submodule depends on the size and complexity of the input image. Large images may take longer to process, and complex images may require more computational resources.

## Roadmap
* Improve the performance of the submodule by optimizing the image processing algorithms.
* Add support for more image formats, such as PNG and JPEG.
* Develop a GUI interface for the submodule to make it easier to use.
* Integrate the submodule with other AIERA CAD modules to create a comprehensive CAD system.
* Develop a web-based version of the submodule to make it accessible to a wider audience.

## License
This submodule is licensed under the MIT License. See LICENSE for more information.

---
**Last updated:** 2026-07-20
