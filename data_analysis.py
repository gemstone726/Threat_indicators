import load_feather as lf
import re
import numpy as np

data = lf.open_feather('19_july_data.feather')

tracks = lf.open_feather('19_july_tracks.feather')

important_track_ids = lf.pull_out_important_tracks(tracks,lf.tracks_out)

db_track_list = important_track_ids['Maybe Name'].to_list()
first_db_track = db_track_list[0]
last_db_track = db_track_list[-1]


test = lf.pull_out_important_data(data, important_track_ids)
_,rcs_min,sv3_min,sva_min,velox_min,veloy_min,velowz_min,rcs_max,sv3_max,sva_max,velox_max,veloy_max,velowz_max = lf.min_max_mean(test)
#gets the first track id and finds its index
first_list = test.loc[test['ID'].str.contains(str(first_db_track))].index.tolist()
first_index = first_list[0]
#gets the last track id and finds its last index location
last_list = test.loc[test['ID'].str.contains(str(last_db_track))].index.tolist()
last_index = last_list[-1]

#gets a subset of the data from the first to last index of interest
sub_setof_data = data.loc[first_index:last_index, :]
unique_data = sub_setof_data.ID.unique()

def filtered_data(df,rcs_min,rcs_max,sv3_min,sv3_max,sva_min,sva_max,velox_min,velox_max,veloy_min,veloy_max,velowz_min,velowz_max):
    df = df[(df['RCS'] >= rcs_min)]
    df = df[(df['RCS'] <= rcs_max)]
    df = df[(df['SV3'] >= sv3_min)]
    df = df[(df['SV3'] <= sv3_max)]
    df = df[(df['SVA'] >= sva_min)]
    df = df[(df['SVA'] <= sva_max)]
    df = df[(df['Altitude'] >= 45)]
    df = df[(df['Altitude'] <= 400)]
    df = df[(df['Velocity_X'] >= velox_min)]
    df = df[(df['Velocity_X'] <= velox_max)]
    df = df[(df['Velocity_Y'] >= veloy_min)]
    df = df[(df['Velocity_Y'] <= veloy_max)]
    df = df[(df['Velocity_Z'] >= velowz_min)]
    df = df[(df['Velocity_Z'] <= velowz_max)]
    return(df)

filtered_data_df = filtered_data(sub_setof_data,rcs_min,rcs_max,sv3_min,sv3_max,sva_min,sva_max,velox_min,velox_max,veloy_min,veloy_max,velowz_min,velowz_max)
sg_filtered_df = filtered_data(sub_setof_data, rcs_min=-99, rcs_max=99, sv3_min=-999,sv3_max=25,sva_min=0,sva_max=99999,velox_min=velox_min,velox_max=velox_max,veloy_min=veloy_min,veloy_max=veloy_max,velowz_min=velowz_min,velowz_max=velowz_max)

print('My Filter Suggestions')
y,_,_,_,_,_,_,_,_,_,_,_,_ = lf.min_max_mean(filtered_data_df)
print(y)

print('Current Singapore Filter Settings')
x,_,_,_,_,_,_,_,_,_,_,_,_ = lf.min_max_mean(sg_filtered_df)
print(x)

unique_filters = filtered_data_df.ID.unique()
sg_unique_filters = sg_filtered_df.ID.unique()

df = filtered_data_df.groupby('ID').filter(lambda x : len(x)>3)
df_sg = sg_filtered_df.groupby('ID').filter(lambda x : len(x)>3)

#print(db_data['ID'])

print('How many data entries are in the JSON file: {}'.format(data.size))
print('How many data entries are just of drone data: {}'.format(test.size))
print('How many data entries do we truely care about?: {}'.format(sub_setof_data.size))
print('How many of the entries have their own unique track ID: {}'.format(unique_data.size))
print('How many unique track ids do we care about: {}'.format(len(db_track_list)))
print('Unique IDs of filtered track data now: {}'.format(unique_filters.size))
print('Singapore IDs of filtered track data now:{}'.format(sg_unique_filters.size))
print('How many data entries do we have left?: {}'.format(filtered_data_df.size))
print('Singapore data entries we have left?: {}'.format(sg_filtered_df.size))
print('How many of the data entries are drone data?: {}'.format(test.size))
#print('Remove data that doesnt meet filters for 4 detections: {}'.format(df.size))
for track_ids in lf.tracks_out:
    lf.track_of_interest(important_track_ids,df,track_ids)
    lf.track_of_interest(important_track_ids,df_sg,track_ids)





