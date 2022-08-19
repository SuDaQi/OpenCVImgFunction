import cv2
from skimage import measure, color
path = "C:\\Users\\ycwb0484\\Desktop\\0818.jpg"
img = cv2.imread(path)
img_copy = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gauss = cv2.GaussianBlur(img_gray, (5, 5), 1)
img_temp = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)[1]
labels = measure.label(img_temp)
dst = color.label2rgb(labels, bg_label=0)    # bg_label=0要有，不然会有警告
cv2.imshow("666", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
