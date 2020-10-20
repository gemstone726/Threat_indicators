import streamlit as st
import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns
import re
import math
import draw_map as dm
import filters 
import stats
import pull_out_data as pod

tracks_out = [761562,763856,768708,838914,841283,843006,844910,850531,852614,854600,856453]

@st.cache(allow_output_mutation=True)
def open_data_feather(file):
    df = pd.read_feather(file)
    return(df)
@st.cache
def open_tracks_feather(file):
    df = pd.read_feather(file)
    return(df)
@st.cache(allow_output_mutation=True)
def start_up():
    track_data = pd.DataFrame()
    data = open_data_feather('track_detections.feather')
    tracks = open_tracks_feather('tracks.feather')
    important_tracks = pod.pull_out_important_tracks(tracks,tracks_out)
    important_data = pod.pull_out_important_data(data,important_tracks)

    #track_out_string = map(str,tracks_out)
    #real_track_ids = tracks_feather[tracks_feather['True Track ID'].isin(track_ids_string)]
    
    #should try to get rid of this for loop
    for tracks in tracks_out:
        x = pod.track_of_interest(important_tracks,important_data,tracks)
        x.to_csv(str(tracks) + '.csv' ,index=False)
        track_data = track_data.append(x)

    return (data, important_tracks, important_data,track_data)

#Future: Animation
#Future: Actual Stats Built In
#Future: Figure Out How to Make the Data Smaller(only show one radar?)

def main():
    data,important_tracks,important_data,track_data = start_up()
    
    

    

    

    st.title('All Drone Track Data')
    st.dataframe(stats.min_max_mean(track_data))

    
    st.sidebar.markdown('### Drone ID')
    select = st.sidebar.selectbox('Drone ID', tracks_out) 

    
    if not st.sidebar.checkbox('Hide Track Info',False, key = '1'):
        st.title('Drone ID: ' + str(select))
        track_data = pod.track_of_interest(important_tracks,important_data,select)
        st.dataframe(stats.min_max_mean(track_data)) 
        st.write('total number of drone detections: {}'.format(len(track_data)))
    
    first_index = track_data.index[0]
    last_index = track_data.index[-1]
    track_id = track_data.iloc[0]['ID']
    df = pod.all_data_for_a_specific_drone_flight(data, first_index,last_index)
    not_drone = df[~df['ID'].isin([track_id])]

    drone_df, not_drone_df = filters.filters(track_data,not_drone)
    
    dm.lat_long(track_data,drone_df,not_drone_df,track_id)
        

if __name__== "__main__":
    main()