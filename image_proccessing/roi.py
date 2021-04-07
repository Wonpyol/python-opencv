import cv2
import numpy as np

img = cv2.imread("../sample_image/prod.png")

x=320; y=150; w=50; h=50
roi = img[y:y+h, x:x+w]

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))
# cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0))
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()