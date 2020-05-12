#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:26:32 2020

@author: internet

"""
import cv2
import numpy as np

cap = cv2.VideoCapture("blue.mp4")
while(1):

    # Her görüntü çerçevesini(frame) yakala
    _, frame = cap.read()

    # BGR'yi HSV'ye çevir
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSV renk uzayında mavi renk oranını(range) ayarla
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Görüntüde Mavi Objeye Threshold Uygula,beyaz filtre
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Orjinal Görüntüye Bitwise-AND İşlemini Uygula
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
      
cv2.waitKey() 
cv2.destroyAllWindows()