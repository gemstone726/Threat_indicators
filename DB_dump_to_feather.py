# Author Chris Ruby

import json
from pandas import json_normalize
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import multiprocessing as mp
import numpy as np
import math
import re      

#Things that i would like to add 
#Multiprocessing (I believe this will allow the program to run faster)
#Save the data/graphs so that it could be shown and given to the customer (this one is easy)

json1 = 'test.json' # 5 json lines of entry
json2 = 'test2.json' #10,000 json lines of entry
json3 = 'test3.json' #1,000,000 json lines of entry ~ 34 mins 
json4 = 'track_detections.json' #guessing #10,000,000 json lines of entry (guessing ~5.1 hours)
july19 = '19_july.json'
track_detections = 'track_detections.json'
rcs_list = []
sv3_list = []
sva_list = []
vmg_list = []
alt_list = []
dist_list = []
veloX_list = []
veloY_list = []
veloZ_list = []
track_list = []
track_id_list = []
track_df= pd.DataFrame()

def read_db_dump(json_file):
    """Creates a feather file from the json database dump from Defense OS

    Args:
        json_file ([type:json]): [track_detections.json] From the database dump from defense OS
    """

    with open(json_file) as f:
        for line in f:
            one_line = json.loads(line)
            # used to figure out what keys are in the json file
            #print(one_line.keys())
            xtra_df = json_normalize(one_line['xtra'])        
            track = xtra_df['type']
            # used to figure out what values are in the DF
            # print(xtra_df.columns.values) 

            if track[0]== str('track'): #Dont think i need this
                track_id_list.append(str(xtra_df['track.name'])) 
                rcs_list.append(float(xtra_df['track.stats.rcs']))
                sv3_list.append(float(xtra_df['track.stats.sv3']))
                sva_list.append(float(xtra_df['track.stats.sva']))
                vmg_list.append(float(xtra_df['track.stats.vmg']))
                alt_list.append(float(xtra_df['track.geolocation.altitude']))
                dist_list.append(float(xtra_df['track.observation.range']))
                veloX_list.append(float(xtra_df['track.geolocation.velocity.x']))
                veloY_list.append(float(xtra_df['track.geolocation.velocity.y']))
                veloZ_list.append(float(xtra_df['track.geolocation.velocity.z']))

    total_raw_data = pd.DataFrame()
    total_raw_data['ID'] = track_id_list
    #would like to figure out how to make this work
    #total_raw_data['ID'] = re.search(r'(\d+)\\n',str(total_raw_data['ID'])).group(1)
    total_raw_data['RCS'] = rcs_list
    total_raw_data['SV3'] = sv3_list
    total_raw_data['SVA'] = sva_list
    total_raw_data['VMG'] = vmg_list
    total_raw_data['Altitude'] = alt_list
    total_raw_data['Distance'] = dist_list
    total_raw_data['Velocity_X'] = veloX_list
    total_raw_data['Velocity_Y'] = veloY_list
    total_raw_data['Velocity_Z'] = veloZ_list

    total_raw_data.to_feather('19_july_data.feather')

def main():

    pool = mp.Pool(mp.cpu_count())
    #trying multiprocessing
    result = pool.map(read_db_dump,[track_detections])  

if __name__ == '__main__':
    main()