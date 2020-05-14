#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:43:41 2020

@author: internet
"""
# import the necessary packages
import numpy as np
import cv2

image = cv2.imread("baloon.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#for red:  lower=[175,0,0] and upper=[255,255,255] that mean [gbr] between[175<g<255,0<g<255,0<r<255]
#for green:lower=[,,] and upper=[,,] g:255 140 b:70 120 r:130 190
#gbr
lower = np.array([170,0,0], dtype = "uint8")
upper = np.array([255,255,255], dtype = "uint8")

mask = cv2.inRange(hsv, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)

cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("my-image3.png",output)