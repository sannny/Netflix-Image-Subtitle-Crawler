from operator import index
import xlsxwriter
import pandas as pd
import datetime
from creds import *



"""
in a loop

check if the next sentence is same as this

if not take its start time as your end time

if so repeat the above process.
"""
        

def convertSecondsToMinutes(time):
    return str(datetime.timedelta(seconds=float(time)))




"""
Unit tests

wrong format

pass in null

pass in just a number

pass in empty list

wrong len more or less

pass in a dict, set wrong datatype

"""



def getting_end_time(val_list):
    hin_intervals = []
    final_output = []
        #['start_time(sec)','end_time(sec)','start_time','end_time','caption']]
    vlen = len(val_list)
    start_time = ''
    end_time = None
    update_flag = 0
    curr = 0
    while curr < vlen:
        #print('index',curr)
        if curr == vlen-1:
            if update_flag == 0:
                start_time = val_list[curr][0]
            end_time = val_list[curr][0]+2.0
        
        elif val_list[curr][2] == val_list[curr+1][2]:
            if update_flag == 0:
                start_time = val_list[curr][0]
                update_flag = 1
            curr+=1
            continue
        else:
            if update_flag == 0:
                start_time = val_list[curr][0]
        
        if end_time == None:
            end_time = val_list[curr+1][0]-0.001
        #print('start_time',convertSecondsToMinutes(start_time))
        #print('end_time',convertSecondsToMinutes(end_time))
        hin_intervals.append([start_time,end_time])
        final_output.append([start_time,end_time,convertSecondsToMinutes(start_time),convertSecondsToMinutes(end_time),val_list[curr][2]])
        start_time = ''
        end_time = None
        update_flag = 0
        curr+=1

    return final_output,hin_intervals

def writeCSV(filename,final_output):

    with open(filename, 'w') as csvfile:

        df = pd.DataFrame(final_output).dropna() 
        df.to_excel(ss_dir_path_win+filename+".xlsx", engine='xlsxwriter')


def getCleanHindiSubs(filename_clean_hindi):
    xl_file = pd.read_excel(filename_clean_hindi, sheet_name = 'Sheet1')
    hin_vals = xl_file.sort_values(by=['time(sec)'], ascending=True).values.tolist()
    return getting_end_time(hin_vals)

#hindi_subs,hin_intervals = getCleanHindiSubs(filename_clean_hindi)

#writeCSV('pilot_ep_1_w_endtime',hindi_subs)

        

