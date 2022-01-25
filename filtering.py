import cv2
import numpy as np
from creds import *


#filePath = ''.join([ss_dir_path,'\\','16_547.png'])

class filter_image:

    
    def __init__(self,img):
        self.img = img

    def applyingFilters(self,img):

        image = img

        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        #Remove Salt and pepper noise
        saltpep = cv2.fastNlMeansDenoising(gray,None,9,13)
        
        #blur
        blured = cv2.blur(saltpep,(3,3))
        
        #binary
        ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
        
        #dilation
        kernel = np.ones((5,100), np.uint8)
        img_dilation = cv2.dilate(thresh, kernel, iterations=1)


        #find contours
        ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #sort contours
        sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])

        for i, ctr in enumerate(sorted_ctrs):

            # Get bounding box
            x, y, w, h = cv2.boundingRect(ctr)

            # Getting ROI
            roi = image[y:y+h, x:x+w]

            im = cv2.resize(roi,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
            ret_1,thresh_1 = cv2.threshold(im,127,255,cv2.THRESH_BINARY_INV)
            # original_resized = cv2.resize(thresh, (0,0), fx=.2, fy=.2)
        
            kernel = np.ones((10, 20), np.uint8)
            words = cv2.dilate(thresh_1, kernel, iterations=1)

            words=cv2.cvtColor(words, cv2.COLOR_BGR2GRAY);

            #find contours
            ctrs_1, hier = cv2.findContours(words, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            #sort contours
            sorted_ctrs_1 = sorted(ctrs_1, key=lambda ctr: cv2.boundingRect(ctr)[0])

            for j, ctr_1 in enumerate(sorted_ctrs_1):

                # Get bounding box
                x_1, y_1, w_1, h_1 = cv2.boundingRect(ctr_1)

                # Getting ROI
                roi_1 = thresh_1[y_1:y_1+h_1, x_1:x_1+w_1]

                chars = cv2.cvtColor(roi_1, cv2.COLOR_BGR2GRAY);

                # dilation
                kernel = np.ones((10, 1), np.uint8)
                joined = cv2.dilate(chars, kernel, iterations=1)


                # find contours
                ctrs_2, hier = cv2.findContours(joined, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # sort contours
                sorted_ctrs_2 = sorted(ctrs_2, key=lambda ctr: cv2.boundingRect(ctr)[0])



                for k, ctr_2 in enumerate(sorted_ctrs_2):
                    # Get bounding box
                    x_2, y_2, w_2, h_2 = cv2.boundingRect(ctr_2)

                    # Getting ROI
                    roi_2 = roi_1[y_2:y_2 + h_2, x_2:x_2 + w_2]


        return roi_2


