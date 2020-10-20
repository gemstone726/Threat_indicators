import pandas as pd
import json 
from pandas import json_normalize
import time
time_list = []

with open('test.json') as f:
        for line in f:
            one_line = json.loads(line)

                # used to figure out what keys are in the json file
                #print(one_line.keys())
            xtra_df = json_normalize(one_line['xtra'])        
            track = xtra_df['type']
                # used to figure out what values are in the DF
                # print(xtra_df.columns.values) 
            time_list.append(float(xtra_df['track.timestamp']))

total_raw_data = pd.DataFrame()
total_raw_data['time'] = time_list
print(time_list)
total_raw_data['time'] = pd.to_datetime(total_raw_data['time'], unit = 'us')
print(total_raw_data)