# Author Chris Ruby

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import math

tracks_out = [856337,857307,857730,858190,858908,859740,860316,862043,862652,862844,863428]
tracks_in = [868442,869652,869799,877672,878506,878623,878985,917116,921630,928958]
tracks_out.extend(tracks_in)

#Name really means Track ID we saw on DEFOS
#Maybe Name means Track ID in Data Base

def open_feather(file):
    """Reads in a feather file and creates it as a pandas dataframe 

    Args:
        file ([type:.feather]): [feather file created in DB_dump_to_feather.py, tracksDB_to_feather.py]
    Return: pandas DataFrame
    """
    df = pd.read_feather(file)
    return(df)

#Creates a Data Frame of the Tracks ID of those Found on the C2 and those that are in the database
def pull_out_important_tracks(tracks_feather, tracks_data):
    """

    Args:
        tracks_feather ([type: DataFrame]): [description]
        tracks_data ([type: list]): [description]
    """
    real_track_ids= pd.DataFrame()
    for track_ids in tracks_data:
        df = tracks_feather[tracks_feather['True Track ID'].str.contains(str(track_ids))]
        real_track_ids = real_track_ids.append(df)
    return(real_track_ids)

#Creates a DataFrame Striping out all the Track Ids that were not Seen on the C2
def pull_out_important_data(data_feather, real_track_ids_DF):
    tracks_I_care_about = pd.DataFrame()
    db_track_ids = real_track_ids_DF['Track ID in Data Bsse'].tolist()
    for track_ids in db_track_ids:
        df = data_feather[data_feather['ID'].str.contains(str(track_ids))]
        tracks_I_care_about = tracks_I_care_about.append(df)
        
    return(tracks_I_care_about)

#Creates a Data Frame of the data dealing with just 1 track id of interest
def track_of_interest(real_track_ids_DF, tracks_I_care_about_DF, track_ID):
    track_of_interest_DF = pd.DataFrame()
    # look for track ID in real_track_ids_DF
    df = real_track_ids_DF[real_track_ids_DF['True Track ID'].str.contains(str(track_ID))]
    # store the track that is seen in the Data Base
    DB_track_o_interest = df['Track ID in Data Bsse'].to_list()
    # search tracks_I_care_about for the track that is in database
    track_of_interest_DF = tracks_I_care_about_DF[tracks_I_care_about_DF['ID'].str.contains(str(DB_track_o_interest[0]))]
    print('Track ID: {} has {} detections'.format(track_ID, track_of_interest_DF.size))
    return(track_of_interest_DF)

def min_max_mean(df):
    
    martix = [(df['RCS'].min(), df['SV3'].min(), df['SVA'].min(), df['VMG'].min(),df['Altitude'].min(), df['Distance'].min(), df['Velocity_X'].min(), df['Velocity_Y'].min(), df['Velocity_Z'].min()), 
              (df['RCS'].max(), df['SV3'].max(), df['SVA'].max(), df['VMG'].max(),df['Altitude'].max(), df['Distance'].max(), df['Velocity_X'].max(), df['Velocity_Y'].max(), df['Velocity_Z'].max()),
              (df['RCS'].mean(), df['SV3'].mean(), df['SVA'].mean(), df['VMG'].mean(),df['Altitude'].mean(), df['Distance'].mean(), df['Velocity_X'].mean(), df['Velocity_Y'].mean(), df['Velocity_Z'].mean())
    ]
    min_max_data = pd.DataFrame(martix, index=list(['Min', 'Max', 'Mean']), columns=list(['RCS', 'SV3', 'SVA', 'VMG', 'Alt', 'Dist', 'Velo_X', 'Velo_Y', 'Velo_Z']))
    return(min_max_data)#, df['RCS'].min()), df['SV3'].min(), df['SVA'].min(),df['Velocity_X'].min(), df['Velocity_Y'].min(), df['Velocity_Z'].min(), df['RCS'].max(), df['SV3'].max(), df['SVA'].max(),df['Velocity_X'].max(), df['Velocity_Y'].max(), df['Velocity_Z'].max())

def print_graphs(df):
    sns.pairplot(df)
    


def main():
    # This is just a proof of concept of what I believe that I can bring to the team below are some more of my ideas if i can get a green light to code at bst
    # Need to clear up some of my variables to make more sense to people 
    # Want to take more data from the json file to get a better picture of our actual data
    # Want to look into Multiprocessing(I believe) to make this program more time efficent
    # Want to save the data so we can look back on it 
    # Want to combine all 3 python scripts together so you only have to run 1 command
    # Want to have the system check if feather file has already been created to not go through the whole process again
    # Want to add the abilty to accept commandline tracks id 
    # Want to add if you want to look at all the tracks ids data or just one
    # Want to be able to look at what is not a drones data to compare to
    # Want to be able to look at what actually get filtered out when you adjust what filter
    # Want to make a function for velo to have a vector that actually makes since
    # Want to look into different types of filters such as weighted averaging and smoothing filters on data to see if we cna make things more accurate and not over fit 
   
    track_id = tracks_out[0]
    

    data = open_feather('19_july_data.feather')
    tracks = open_feather('tracks.feather')

    important_tracks = pull_out_important_tracks(tracks,tracks_out)

    important_data = pull_out_important_data(data, important_tracks)

    #prints min max mean of all the data dealing with all the Track ID recorded
    track_data= pd.DataFrame()
    for tracks in tracks_out:
        x = track_of_interest(important_tracks,important_data,tracks)
        track_data = track_data.append(x)
        #print(min_max_mean(x))
        #print('========================================================================================================================')
    print(min_max_mean(track_data))
    #track_of_interest_df = track_of_interest(important_tracks,important_data,track_id)

    #Prints Just the Track of interest Min Mean Max of just 1 track we care about

    #print('All Data Collected')
    #print(min_max_mean(data))
    #print(important_data)
    #print('========================================================================================================================')
    print('All Track_Ids Data')
    print(min_max_mean(important_data))
    #print('========================================================================================================================')
    #print('Track of Interest {}'.format(track_id))
    #print(min_max_mean(track_of_interest_df))
    #print_graphs(track_of_interest_df)
    #plt.show()


if __name__ == '__main__':
    main()


