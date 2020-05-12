#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:26:32 2020

@author: internet
"""

import cv2
import numpy as np

filename = 'lego.jpeg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow("lego!",img)
cv2.waitKey()
cv2.destroyAllWindows()
