# Grip_Foundation_Task-2_June-2021
 Implement an image color detector which identifies all the colors in an  image or video.

# I have used numpy and computer vision for my project
# imported them using import function

       import numpy as np
       import cv2 as cv

  # defined my parameter here named it as click_event

        def click_event(event, x, y, flag, param):
            if event == cv.EVENT_LBUTTONDOWN:

# defined 3 variables blue green red and stored img list in it with y & x as the points

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
