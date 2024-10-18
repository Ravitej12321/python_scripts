import cv2
import numpy as np

image = cv2.imread('C:\\Users\\ADMIN\\Downloads\\PassportPhoto.jpg')
croped_image = image#[100:500,100:600]
# cv2.imshow("image",image)
image = cv2.cvtColor(croped_image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("image2",image)
blur_image = cv2.GaussianBlur(image,(3,3),0)
cv2.imshow("blur_image",blur_image)
sobel_x = cv2.Sobel(blur_image,ddepth=cv2.CV_64F,dx=3,dy=0,ksize=5)
sobel_y = cv2.Sobel(blur_image,ddepth=cv2.CV_32F,dx=0,dy=3,ksize=5)
sobel_xy= cv2.Sobel(blur_image,ddepth=cv2.CV_64F,dx=3,dy=3,ksize=5)
canny_edges = cv2.Canny(blur_image,threshold1=50,threshold2=170)
cv2.imshow("canny Edges",canny_edges)
# cv2.imshow("sobel in y",sobel_y)
cv2.imshow("sobel in xy",sobel_xy)
# cv2.imshow("sobel in x",sobel_x)
cv2.waitKey(0)