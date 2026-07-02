from skeleton_furniture.pipeline import Pipeline
import cv2

# Load the input image
image = cv2.imread('input_image.jpg')

# Create a Pipeline object
pipeline = Pipeline(image)

# Process the image
contours = pipeline.process()

# Display the contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
 cv2.imshow('Contours', image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()