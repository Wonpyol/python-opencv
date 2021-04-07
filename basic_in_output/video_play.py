import cv2

video_file = "../sample_video/mss.mp4"
cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(30)
        else:
            break
else:
    print("cat't open video")

cap.release()
cv2.destroyAllWindows()
