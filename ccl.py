import cv2
import numpy as np

img = cv2.imread('Kmean\\seg.png',0)

#path = cv2.imread('seg1.png')
#img=cv2.GaussianBlur(img,(5,5),0)
#cv2.imshow('old',image)

img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]  # ensure binary
#cv2.imshow('new',img)
ret, labels = cv2.connectedComponents(img)

def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue==0] = 0

    #cv2.imwrite('labeled.png', labeled_img)

    src = labeled_img
    tmp = cv2.cvtColor(labeled_img, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    cv2.imwrite("CCl\\trans.png", dst)
    cv2.waitKey()
    

imshow_components(labels)
