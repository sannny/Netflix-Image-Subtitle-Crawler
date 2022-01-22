from operator import index
import xlsxwriter
import pandas as pd
import datetime

filename = 'D:\\linux\\scratches\\Netflix_image_subtitle_crawler\\Screenshots\\pilot_ep_1.xlsx'

xl_file = pd.read_excel(filename, sheet_name = 'Sheet1')



hin_vals = xl_file.sort_values(by=['time(sec)'], ascending=True).values.tolist()

print(len(hin_vals))

"""
in a loop

check if the next sentence is same as this

if not take its start time as your end time

if so repeat the above process.
"""



def timeStr_sanity_check(timestr):
    coln_split = timestr.split(':')
    if len(coln_split) == 3:
        if '.' in coln_split[-1]:
            return timestr
        else:
            return ''.join([timestr,'.000000'])
    else:
        no_of_appends = 3 - len(coln_split)
        i = 1
        while i <= no_of_appends:
            if i == no_of_appends:
                timestr = ''.join([timestr,'00.000000'])
            else:
                timestr = ''.join([timestr,'00:'])
            i+=1
    return timestr
        

def convertSecondsToMinutes(time):
    return str(datetime.timedelta(seconds=float(time[:-4])))

"""
Unit tests

wrong format

pass in null

pass in just a number

"""
def str_to_time(time_Str):
    return datetime.datetime.strptime(timeStr_sanity_check(time_Str),'%H:%M:%S.%f')

"""
Unit tests

wrong format

pass in null

pass in just a number

"""
def datetime_add(start,diff):
    time_zero = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
    return  ((str_to_time(start) - time_zero + str_to_time(diff)).time())

#print(type(datetime_add('0:19:40.032000','00:00:02.000000')))

final_output = [['start_time','end_time','caption']]

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
    vlen = len(val_list)
    start_time = ''
    end_time = None
    update_flag = 0
    curr = 0
    while curr < vlen:
        if curr == vlen-1:
            end_time = datetime_add(val_list[curr][0],'00:00:02.000000')
        
        elif val_list[curr][2] == val_list[curr+1][2]:
            if update_flag == 0:
                start_time = val_list[curr][0]
                update_flag = 1
            curr+=1
            continue
        else:
            start_time = val_list[curr][0]
        
        if end_time == None:
            end_time = str_to_time(val_list[curr+1][0]).time()
        print(start_time)
        final_output.append([str_to_time(start_time).time(),end_time,val_list[curr][2]])
        start_time = ''
        end_time = None
        update_flag = 0
        curr+=1

getting_end_time(hin_vals)
print(final_output)

        




