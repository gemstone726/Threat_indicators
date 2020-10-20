import streamlit_load_feather as slf
import numpy as np
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pyplot
import math

@st.cache
def init_load():
    data = slf.open_data_feather('19_july_data.feather')
    tracks = slf.open_tracks_feather('tracks.feather')
    important_track_ids = slf.pull_out_important_tracks(tracks,slf.tracks_out)

    db_track_list = important_track_ids['Track ID in Data Bsse'].to_list()
    first_db_track = db_track_list[0]
    last_db_track = db_track_list[-1]
    
    all_track_data = slf.pull_out_important_data(data,important_track_ids)

    #first index of the first track ID
    first_index = all_track_data.loc[all_track_data['ID'].str.contains(str(first_db_track))].index.tolist()[0]

    #last index of the last track ID
    last_index = all_track_data.loc[all_track_data['ID'].str.contains(str(last_db_track))].index.tolist()[-1]

    sub_setof_data = data.loc[first_index:last_index, :]
    st.write(sub_setof_data)
    print(sub_setof_data)




def main():
    init_load()



    
if __name__=='__main__':
    main()

