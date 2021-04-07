import cv2
import numpy as np

img = cv2.imread("../sample_image/prod.png")

x=320; y=150; w=50; h=50
roi = img(y:y+h, x:x+w)
img2 = roi.copy()