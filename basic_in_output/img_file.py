import cv2

img_file = "../sample_image/prod.png"
save_file = "../sample_image/prod_gray.png"
# mode flag
# cv2.IMREAD_COLOR : BGR 컬러로 읽기, 기본 값
# cv2.IMREAD_UNCHANGED : 파일 그래로 읽기
# cv2.IMREAD_GRAYSCALE : 흑백으로 읽기

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.imwrite(save_file, img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("No image File" )

