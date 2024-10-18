# import cv2 as cv
# import numpy as np

# image = cv.imread("C:\\Users\\ADMIN\\Desktop\\python Scripts\\Opencv\\addedalone.jpg",cv.IMREAD_GRAYSCALE)
# if image is not None:
#     detector = cv.SimpleBlobDetector()
#     keypoints = detector.detect(image)
#     output  = cv.drawKeypoints(image,keypoints,np.array([]),(0,0,255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     cv.imshow('output',output)
#     cv.waitKey(0)
# else:
#     print("error loading image")
# Standard imports
import cv2
import numpy as np
# Load image
image = cv2.imread('C:\\Users\\ADMIN\\Desktop\\python Scripts\\Opencv\\nathan-fertig-scbYOgVyb8Q-unsplash.jpg')

# Check if image is loaded correctly
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Setup SimpleBlobDetector parameters
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200

# # Filter by Area.
# params.filterByArea = True
# params.minArea = 1500

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
try:
    keypoints = detector.detect(gray_image)
except cv2.error as e:
    print(f"OpenCV Error: {e}")
    exit()

# Draw detected blobs as red circles
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(gray_image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display image with blobs
cv2.imshow("Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()