import pandas as pd
import streamlit as st

@st.cache
def pull_out_important_tracks(tracks_feather, tracks_id_list):
    real_track_ids= pd.DataFrame()
    track_ids_string = map(str,tracks_id_list)
    real_track_ids = tracks_feather[tracks_feather['True Track ID'].isin(track_ids_string)]
    return(real_track_ids)

@st.cache(allow_output_mutation=True)
def pull_out_important_data(data_feather, real_track_ids_DF):

    tracks_I_care_about = pd.DataFrame()
    real_track_ids = real_track_ids_DF['Track ID in Data Base'].to_list()
    tracks_I_care_about = data_feather[data_feather['ID'].isin(real_track_ids)]
    return(tracks_I_care_about)

@st.cache   
def track_of_interest(real_track_ids_DF, tracks_I_care_about_DF, track_ID):
    track_of_interest_DF = pd.DataFrame()
    try:
        # look for track ID in real_track_ids_DF
        df = real_track_ids_DF[real_track_ids_DF['True Track ID'].str.match(str(track_ID))]
        # store the track that is seen in the Data Base
        DB_track_o_interest = df['Track ID in Data Base'].to_list()
        # search tracks_I_care_about for the track that is in database
        track_of_interest_DF = tracks_I_care_about_DF[tracks_I_care_about_DF['ID'].str.match(str(DB_track_o_interest[1]))]
        #print('Track ID: {} has {} detections'.format(track_ID, len(track_of_interest_DF)))
    except Exception as e:
        print(track_ID)
        print(str(e))
    return(track_of_interest_DF)


@st.cache
def all_data_for_a_specific_drone_flight(df, first_index, last_index):
    df= df.loc[first_index:last_index, :]
    return(df)