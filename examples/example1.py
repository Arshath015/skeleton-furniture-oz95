from skeleton_furniture.skeletonizer import Skeletonizer
import cv2

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