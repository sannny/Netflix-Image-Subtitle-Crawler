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
# import coverage

# cov = coverage.Coverage()
# cov.start()



sys.stdout.reconfigure(encoding='utf-8')


#pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

csv_rows = [['time(sec)','time','captions']]

def creatingFilesPath(fileName):
    return ''.join([ss_dir_path,'/',fileName])


def croppingimg(image):
    height,width = image.shape[0],image.shape[1]
    y0 = 0+(height*0.15)
    y1 = height - (height*0.13)
    delta_width = width*0.20
    return image[int(y0):int(y1), int(0+delta_width):int(width-delta_width)]

def extract_Data(img):
    tesseract_output = pytesseract.image_to_data(image = img,lang='hin',output_type = 'dict')
    return ' '.join(tesseract_output['text']).strip()

def openImg(path):
    return cv2.imread(path)

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
    final = [float(time.replace('_','.')[:-4]),convertSecondsToMinutes(time.replace('_','.')),text]#clean_text(text)]
    csv_rows.append(final)

def writeCSV(filename):

    filepath = ''.join([filename,".xlsx"])
    with open(filepath, 'w') as csvfile:
        
        df = pd.DataFrame(csv_rows)  
        df.to_excel(filepath, engine='xlsxwriter')
        # creating a csv writer object  
        #csvwriter = csv.writer(csvfile)  
            
        # writing the fields  
        #csvwriter.writerow(csv_rows)  
    
def start_extraction():
    rename = renaming()
    rename.switch_to_ss_dir()
    files = rename.list_all_files()
    fl = len(files)
    filter = filter_image(None)
    for i,file in enumerate(files):
        if '.png' in file:
            appendRow(extract_Data(filter.applyingFilters(croppingimg(openImg(creatingFilesPath(file))))),file)
            print(i,'files of ',fl,'read')
    writeCSV(creatingFilesPath('pilot_ep_1'))


#start_extraction()
    
# cov.stop()
# cov.save()

# cov.html_report()


        


#rename = renaming()
#rename.switch_to_ss_dir()
#files = rename.list_all_files()
"""filePath = ''.join([ss_dir_path,'\\','180_912.png'])
img = cv2.imread(filePath)
#y0,x0,x1,y1 = reducingimg(10,img.shape[0],img.shape[1])
filtered = filter_image(img)
cropped_image = filtered.applyingFilters(croppingimg(img))
# Cropping an image
#cropped_image = img[x0:x1, y0:y1]
#cv2.imshow("Display window",cropped_image)
#k = cv2.waitKey(0)
tesseract_output = pytesseract.image_to_data(image = cropped_image,lang='hin',output_type = 'dict')
#combining_marks = (' '.join(tesseract_output['text'])).encode('raw-unicode-escape').decode('utf-8').lstrip()
#sys.stdout.buffer.write((' '.join(tesseract_output['text'])).encode('raw-unicode-escape'))
extracted_text = ' '.join(tesseract_output['text']).strip()
appendRow(extracted_text,'180_912.png')
writeCSV(creatingFilesPath('test'))
print(extracted_text)
#cv2.destroyAllWindows()
"""