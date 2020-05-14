# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:31:14 2020

@author: best
"""
import cv2 as cv
import numpy as np

img_rgb = cv.imread('circuit.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('circuititem.jpg',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

a=0
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    a=1+a

cv.imwrite('detectedpic.png',img_rgb)
print(a)
