# Author Chris Ruby
import json
import pandas as pd
from pandas import json_normalize

track_file = 'tracks.json'
name = []
maybe_name = []



with open(track_file) as f:
    for line in f:
        one_line = json.loads(line)
        #sensor = json_normalize(one_line['sensor_cfg'])        
        
        name.append(str(one_line['name']))
        
        # Get stuff from sources.tracks
        sensor_df =(one_line['sensor_cfg']['sources'])
        sensor_df= pd.DataFrame(sensor_df['tracks'])
        name_maybe = sensor_df['name']
        
        maybe_name.append(str(name_maybe.get(0)))
        
        #this works just dont think i need it 
        #sensor_id = sensor_df['sensorId']
        
raw_data = pd.DataFrame()
raw_data['True Track ID'] = name
raw_data['Track ID in Data Bsse'] = maybe_name

raw_data.to_feather('tracks.feather')

