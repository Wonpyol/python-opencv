import cv2

img = cv2.imread("../sample_image/prod.png")
x,y,w,h = cv2.selectROI("img", img, False)
print("x:%d,y:%d,w:%d,h:%d" % (x,y,w,h))

if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow("cropped", roi)
    cv2.moveWindow("cropped", 0, 0)
    cv2.imwrite("./croped3.jpg", roi)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

