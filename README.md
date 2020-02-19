Python script for measuring vascular bundle vessel diameter (Python 3.7.x)
November 2019

Written by Santiago Campuzano

Open Computer Vision (OpenCV) based Python script for measuring the area of Contours (enclosed structures). The script takes the path to an image (i.e. the location in the computer), applies Canny edge detection to the image (Binary image containing edges), and draws contours around an enclosed structure. Prior to exporting data in the form of an xlsx file, an area- threshold is set based on the size of the smallest and largest vessel diameter to reduce noise. OpenCV supports TIFF, JPEG, PNG and JPEG2000. To find out more about imag- file reading, refer to the documentation page: https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
