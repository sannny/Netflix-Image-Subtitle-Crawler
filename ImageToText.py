import pytesseract
import cv2 
from creds import *
from os_ss_refactoring import *
import numpy
import re
import sys
import csv
import datetime
import pandas as pd
import xlsxwriter
from filtering import *
import string
from html.parser import HTMLParser 
import re



sys.stdout.reconfigure(encoding='utf-8')


#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

csv_rows = [['time(sec)','time','captions']]

def reducingimg(perc,height,width):
    red_height = height*(perc/100)
    red_width = width*(perc/100)
    return int(red_height),int(red_width)+171,int(height-red_height),int(width-red_width)

def creatingFilesPath(fileName):
    return ''.join([ss_dir_path,'\\',fileName])

def croppingimg(img,perc):
    y0,x0,x1,y1 = reducingimg(perc,img.shape[0],img.shape[1])
    return img[x0:x1, y0:y1]

def extract_Data(img):
    tesseract_output = pytesseract.image_to_data(image = img,lang='hin',output_type = 'dict')
    return ' '.join(tesseract_output['text']).strip()

def openImg(path):
    return cv2.imread(path,0)

def convertSecondsToMinutes(time):
    return str(datetime.timedelta(seconds=float(time[:-4])))

def clean_text(text):

    hp = HTMLParser()

    new_text = hp.unescape(text).split()

    chars = re.escape(string.punctuation)

    rm_ind = []

    for i,subtext in enumerate(new_text):
        con_text = str(re.sub(r'['+chars+']', ' ',subtext).encode('raw-unicode-escape').decode('utf-8')).split(' ')
        l = len(con_text[0])
        count = 0
        ind = 0
        while ind <= l-2:
            if con_text[0][ind:ind+2] == '\\u':
                count+=1
                ind+=6
            else:
                ind+=1
        if count < 2:
            rm_ind.append(i)

    for ind in reversed(rm_ind):
        del new_text[ind]
    
    return ' '.join(new_text)

    

def appendRow(text,time):
    final = [float(time.replace('_','.')[:-4]),convertSecondsToMinutes(time.replace('_','.')),clean_text(text)]
    csv_rows.append(final)

def writeCSV(filename):

    with open(filename, 'w') as csvfile:

        df = pd.DataFrame(csv_rows)  
        df.to_excel(filename+".xlsx", engine='xlsxwriter')
        # creating a csv writer object  
        #csvwriter = csv.writer(csvfile)  
            
        # writing the fields  
        #csvwriter.writerow(csv_rows)  
    
def start_extraction():
    rename = renaming()
    rename.switch_to_ss_dir()
    files = rename.list_all_files()
    fl = len(files)
    for i,file in enumerate(files):
        appendRow(extract_Data(croppingimg(openImg(creatingFilesPath(file)),10)),file)
        print(i,'files of ',fl,'read')
    writeCSV(creatingFilesPath('pilot_ep_1'))


start_extraction()
    



        


"""rename = renaming()
rename.switch_to_ss_dir()
files = rename.list_all_files()
filePath = ''.join([ss_dir_path,'\\','16_547.png'])
img = cv2.imread(filePath,0)
y0,x0,x1,y1 = reducingimg(10,img.shape[0],img.shape[1])
filtered = filter_image(filePath)
cropped_image = filtered.applyingFilters()
# Cropping an image
#cropped_image = img[x0:x1, y0:y1]
#cv2.imshow("Display window",cropped_image)
#k = cv2.waitKey(0)
tesseract_output = pytesseract.image_to_data(image = cropped_image,lang='hin',output_type = 'dict')
#combining_marks = (' '.join(tesseract_output['text'])).encode('raw-unicode-escape').decode('utf-8').lstrip()
#sys.stdout.buffer.write((' '.join(tesseract_output['text'])).encode('raw-unicode-escape'))
extracted_text = ' '.join(tesseract_output['text']).strip()
appendRow(extracted_text,'16_547.png')
writeCSV(creatingFilesPath('test'))
print(extracted_text)
#cv2.destroyAllWindows()"""
