import numpy as np
import cv2 as cv


def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        imageBGR = np.zeros((250, 250, 3), np.uint8)
        imageBGR[:] = [blue, green, red]

        cv.imshow("BGR colors", imageBGR)


img = cv.imread("wallpaper.jpeg")
cv.imshow("WINDOW 2", img)
cv.setMouseCallback("WINDOW 2", click_event)
cv.waitKey(0)
cv.destroyAllWindows()
