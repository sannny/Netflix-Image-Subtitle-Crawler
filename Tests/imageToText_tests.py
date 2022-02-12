from cgi import test
import unittest
import numpy as np
from PIL import Image
import sys
sys.path.insert(1, 'D:\\linux\\scratches\\Netflix_image_subtitle_crawler')
from ImageToText import *


class cropping_img_tests(unittest.TestCase):
    def test_None(self):
        input = None
        with self.assertRaises(Exception):
            croppingimg(input)

    def test_emptyList(self):
        input = [[],[],[]]
        with self.assertRaises(Exception):
            croppingimg(input)


    def test_alphabets(self):
        input = [
                    ['ab',1,2,34,5,6,78,2,34,56,32,12,43,542,545,53,566,23,435,65,34],
                    [43,122,44,5,5,3,2,45,6,7,7,88,'cd',1234,44,34,556,23,35,23,23],
                    ['ab',1,2,34,5,6,78,2,34,56,32,12,1234,44,34,556,23,35,23,23,266]
                ]
        with self.assertRaises(Exception):
            croppingimg(input)

    def test_numeric(self):
        file = 'D:\\linux\\scratches\\Netflix_image_subtitle_crawler\\Tests\\new_snip.png'
        img = cv2.imread(file) 
        out = np.asarray(croppingimg(img)).all()       
        ans = np.asarray(img[116:677,353:1412]).all()
        self.assertEqual(out,ans)

if __name__ == '__main__':
    tests = cropping_img_tests()
    tests.test_None()
    tests.test_emptyList()
    tests.test_alphabets()
    tests.test_numeric()
