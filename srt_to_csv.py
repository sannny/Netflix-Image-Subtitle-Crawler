from typing import final
import pysrt
import pandas as pd
from cleaning_hindi_csv import *

path = 'D:\\linux\\scratches\\Netflix_image_subtitle_crawler\\pilot_ep_1.srt'

subs = pysrt.open(path)

en_interval = []
captions = []
    #['startTime(sec)','endTime(sec)','startTime','endTime','en_text']]

for sub in subs:
    startTime = sub.start.to_time()
    startTimeSec = (((startTime.hour * 60.0)+startTime.minute)*60)+startTime.second+(startTime.microsecond*.000001)
    endTime = sub.end.to_time()
    endTimeSec = (((endTime.hour * 60.0)+endTime.minute)*60)+endTime.second+(endTime.microsecond*.000001)
    en_interval.append([startTimeSec,endTimeSec])
    cap = [startTimeSec,endTimeSec,startTime,endTime,sub.text]
    captions.append(cap)

hindi_subs,hin_intervals = getCleanHindiSubs(filename_clean_hindi)

def final_interval(en,hin):
    en =  [list( map(float,i) ) for i in en]
    hin =  [list( map(float,i) ) for i in hin]
    comb = []
    hlen = len(hin)
    elen = len(en)
    i = 0
    j = 0
    while i < hlen and j < elen:
        if en[j][0] > hin[i][0]:
            comb.append(hin[i])
            i+=1
        elif en[j][0] < hin[i][0]:
            comb.append(en[j])
            j+=1
        elif en[j][0] == hin[i][0]:
            if en[j][1] > hin[i][1]:
                comb.append(hin[i])
                i+=1
                comb.append(en[j])
                j+=1
            if en[j][1] < hin[i][1]:
                comb.append(en[j])
                j+=1
                comb.append(hin[i])
                i+=1
    while i < hlen:
        comb.append(hin[i])
        i+=1
    while j < elen:
        comb.append(en[j])
        j+=1
    return comb


                

"""
take the combination of lowest and highest.

mix all to cover the extras

"""
def merge(intervals: list[list[float]]) -> list[list[float]]:
        
        intervals =  [list( map(float,i) ) for i in intervals]
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
#print(len(subs))
def writeCSV(filename,final_output):

    with open(filename, 'w') as csvfile:

        df = pd.DataFrame(final_output).dropna() 
        df.to_excel(ss_dir_path_win+filename+".xlsx", engine='xlsxwriter')

def putting_subs_together(intervals,hindi_subs,captions):

    for i,hindi_sub in enumerate(hindi_subs):
        hindi_subs[i][0] = float(hindi_sub[0])
        hindi_subs[i][1] = float(hindi_sub[1])
    
    for i,caption in enumerate(captions):
        captions[i][0] = float(caption[0])
        captions[i][1] = float(caption[1])


    final = [['start_time','end_time','hindi','english']]

    hlen = len(hindi_subs)
    elen = len(captions)

    i = 0
    j = 0

    for bucket in intervals:
        #getting string for end time before bucket max from hin subs
        hin = ''
        en = ''
        while i < hlen and float(bucket[1]) >= float(hindi_subs[i][1]) :
            hin = ' '.join([hin,str(hindi_subs[i][4])])
            i+=1

        while j < elen and float(bucket[1]) >= float(captions[j][1]) :
            en = ' '.join([en,str(captions[j][4])])
            j+=1
        
        final.append(bucket.copy()+[hin,en])
    
    return final



writeCSV('pilot_ep_1_final_script',putting_subs_together(merge(final_interval(en_interval,hin_intervals)),hindi_subs,captions))

#print(captions[1])
#print(hindi_subs[1])