import pysrt

import pandas as pd

path = 'D:\\linux\\scratches\\Netflix_image_subtitle_crawler\\pilot_ep_1.srt'

subs = pysrt.open(path)

captions = [['startTime','endTime','en_text']]

for sub in subs:
    cap = [sub.start.to_time(),sub.end.to_time(),sub.text]
    captions.append(cap)

    



print(len(subs))

print(captions)