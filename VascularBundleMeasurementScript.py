# Python script for measuring vascular bundle vessel diameter (Python 3.7.x)
# November 2019
# Written by Santiago Campuzano
# 
# Open Computer Vision (OpenCV) based Python script for measuring the area of Contours  
# (enclosed structures). The script takes the path to an image (i.e. the location in the computer), 
# applies Canny edge detection to the image (Binary image containing edges), and draws 
# contours around an enclosed structure.
# Prior to exporting data in the form of an xlsx file, an area- threshold is set based on the size
# of the smallest and largest vessel diameter to reduce noise. 
# OpenCV supports TIFF, JPEG, PNG and JPEG2000. To find out more about imag- file reading,
# refer to the documentation page:
# https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html

import cv2
import numpy as np
import pandas as pd
import math

# Declare global variables
areas = []
BelowThr = []
tool = list(range(0, 1000))
df = pd.DataFrame({}, tool)

#open image in provided PATH
img = cv2.imread(‘PATH’)

# Resize image to fit screen
newImgMask = cv2.resize(img, (0,0), fx=0.7, fy=0.7)

#convert to from RGB to BGR
bw = cv2.cvtColor(newImgMask, cv2.COLOR_RGB2BGR)

#Isolate edges using OpenCV's Canny edge detection method
edges = cv2.Canny(bw,200,300)

#find and draw OpenCV Contours
contours, hierachy = cv2.findContours(edges, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(newImgMask, contours, -1, (0,0,255), 1)

# For all of the contours in the "contours" list calculate the area and determine the diameter
based on the correlation between surface area and diameter. In an effort to reduce noise, thresholds for min and max area were set based on manual measurements. Once the diameter is calculated, the values are appended to an excel file (PATH),

for c in contours:
    if ((math.sqrt((cv2.contourArea(c)*1.48)/math.pi))*2) < 10:
        BelowThr.append((math.sqrt((cv2.contourArea(c)*1.48)/math.pi))*2)

    elif ((math.sqrt((cv2.contourArea(c)*1.48)/math.pi))*2) >= 55:
        BelowThr.append((math.sqrt((cv2.contourArea(c) * 1.48) / math.pi)) * 2)

    else:
        areas.append((math.sqrt((cv2.contourArea(c)*1.48)/math.pi))*2)

writer = pd.ExcelWriter("PATH", engine='xlsxwriter')
dataY = np.array(BelowThr)
dataX = np.array(areas)
df['area'] = pd.Series(dataX)
df['BelowThr'] = pd.Series(dataY)

#display the images
cv2.imshow('f',edges)
cv2.imshow('G', newImgMask)
print(areas)

cv2.waitKey(0)

# Write data to excel file on exit
df.to_excel(writer, sheet_name='Sheet1')
print(df)
writer.save()

cv2.destroyAllWindows()























Python script for measuring cell migration through vascular bundle

# Import required packages
import cv2
import pandas as pd
import glob2 as glob
import os
import numpy as np

# Declare global variables and lists
images = []
my_listX = []
my_listY = []
x = 0
y = 0
AddColX = 0
AddColY = 0
tool = list(range(0, 1000))
df = pd.DataFrame({}, tool)

# mouse-click callback function. Each time a mouse click is detected, the function will append the x and y coordinates

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(n,(x,y),2,(0,255,0),-1)
        my_listX.append(x)
        my_listY.append(y)

# Use glob.glob to batch upload images from the declared PATH.
Create separate excel columns for x and y coordinates. 

for img in glob.glob("PATH"):
    writer = pd.ExcelWriter("PATH", engine='xlsxwriter')
    ColX = "(X){}".format(os.path.basename(img))
    ColY = "(Y){}".format(os.path.basename(img))
    Text = "{}".format(img)
    n = cv2.imread(Text)
    cv2.namedWindow(Text)
    cv2.setMouseCallback(Text, draw_circle)
    images.append(Text)
    print(Text)



    while True:
        cv2.imshow(Text, n)

# Once the spacebar is pressed, the list will be added to the excel file
        if cv2.waitKey(10) == 32:
            print(my_listY)
            print(my_listX)
            cv2.destroyWindow(Text)
            dataX = np.array(my_listX)
            dataY = np.array(my_listY)
            df[ColX] = pd.Series(dataX)
            df[ColY] = pd.Series(dataY)
            del my_listY[:]
            del my_listX[:]
            break

df.to_excel(writer, sheet_name='Sheet1')
print(df)
writer.save()
