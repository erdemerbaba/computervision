# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:04:43 2020

@author: best
"""


import cv2
import numpy as np

im = cv2.imread("shape.jpg")
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY);
gray = cv2.GaussianBlur(gray, (5, 5), 0)
_, bin = cv2.threshold(gray,120,255,1) 
bin = cv2.dilate(bin, None)  
bin = cv2.dilate(bin, None)
bin = cv2.erode(bin, None)   
bin = cv2.erode(bin, None)
bin = contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

rc = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rc)
for p in box:
    pt = (p[0],p[1])
    print (pt)
    cv2.circle(im,pt,5,(200,0,0),2)
cv2.imshow("plank", im)
cv2.waitKey()
cv2.destroyAllWindows()
